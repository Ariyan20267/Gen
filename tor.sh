#!/data/data/com.termux/files/usr/bin/bash
# =============================================================================
#  ARIYAN TOR AUTO-ROTATOR  —  Termux Edition
#  প্রতি ১০ সেকেন্ডে নতুন IP, রঙিন বক্সে দেখাবে
# =============================================================================

# ---------- Colors ----------
RST=$'\033[0m'
BOLD=$'\033[1m'
C1=$'\033[38;5;201m'   # magenta
C2=$'\033[38;5;51m'    # cyan
C3=$'\033[38;5;82m'    # green
C4=$'\033[38;5;226m'   # yellow
C5=$'\033[38;5;196m'   # red
C6=$'\033[38;5;208m'   # orange
C7=$'\033[38;5;135m'   # purple

# ---------- Config ----------
SOCKS_PORT=9050
CONTROL_PORT=9051
ROTATE_INTERVAL=10          # সেকেন্ড
TORRC_DIR="$HOME/.tor"
TORRC_FILE="$TORRC_DIR/torrc"
TOR_DATA="$HOME/.tor_data"
TOR_LOG="$HOME/.tor_log"

# ---------- Helpers ----------
log()  { echo "${C2}[*]${RST} $*"; }
ok()   { echo "${C3}[✓]${RST} $*"; }
warn() { echo "${C4}[!]${RST} $*"; }
err()  { echo "${C5}[✗]${RST} $*"; }

box() {
    local color="$1"; shift
    local title="$1"; shift
    local W=48
    local line="$*"
    local pad=$(( W - ${#line} - 2 ))
    [ $pad -lt 0 ] && pad=0
    printf "%s╔════════════════════════════════════════════════╗%s\n" "$color" "$RST"
    printf "%s║%s %s%-${W}s%s %s║%s\n" "$color" "$RST" "$BOLD" "$title" "$RST" "$color" "$RST"
    printf "%s╠════════════════════════════════════════════════╣%s\n" "$color" "$RST"
    printf "%s║%s %-${W}s %s║%s\n" "$color" "$RST" "$line" "$color" "$RST"
    printf "%s╚════════════════════════════════════════════════╝%s\n" "$color" "$RST"
}

# ---------- Banner ----------
banner() {
    clear
    echo "${C1}${BOLD}"
    cat <<'EOF'
   ░█████╗░██████╗░██╗██╗░░░██╗░█████╗░███╗░░██╗
   ██╔══██╗██╔══██╗██║╚██╗░██╔╝██╔══██╗████╗░██║
   ███████║██████╔╝██║░╚████╔╝░███████║██╔██╗██║
   ██╔══██║██╔══██╗██║░░╚██╔╝░░██╔══██║██║╚████║
   ██║░░██║██║░░██║██║░░░██║░░░██║░░██║██║░╚███║
   ╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚══╝
EOF
    echo "${RST}${C2}${BOLD}        ░ TOR AUTO-ROTATOR — TERMUX EDITION ░${RST}"
    echo
}

# ---------- Termux check ----------
check_termux() {
    if [ ! -d "/data/data/com.termux" ]; then
        warn "Termux detect হয়নি — তবুও চেষ্টা করছি..."
    else
        ok "Termux detected"
    fi
}

# ---------- Package install ----------
install_pkgs() {
    log "প্রয়োজনীয় প্যাকেজ চেক করা হচ্ছে..."
    local need=()
    command -v tor     >/dev/null 2>&1 || need+=("tor")
    command -v curl    >/dev/null 2>&1 || need+=("curl")
    command -v python  >/dev/null 2>&1 || command -v python3 >/dev/null 2>&1 || need+=("python")

    if [ ${#need[@]} -eq 0 ]; then
        ok "সব প্যাকেজ আগে থেকেই আছে"
        return 0
    fi

    warn "ইনস্টল করতে হবে: ${need[*]}"
    log "pkg update চালানো হচ্ছে..."
    yes | pkg update -y >/dev/null 2>&1
    for p in "${need[@]}"; do
        log "ইনস্টল: $p"
        yes | pkg install -y "$p" >/dev/null 2>&1
    done

    # পুনরায় verify
    command -v tor  >/dev/null 2>&1 || { err "tor ইনস্টল fail"; exit 1; }
    command -v curl >/dev/null 2>&1 || { err "curl ইনস্টল fail"; exit 1; }
    ok "সব প্যাকেজ ইনস্টল সম্পন্ন"
}

# ---------- torrc তৈরি ----------
write_torrc() {
    log "torrc কনফিগার করা হচ্ছে → $TORRC_FILE"
    mkdir -p "$TORRC_DIR" "$TOR_DATA"

    # ControlPort-এ password ছাড়া auth দরকার
    cat > "$TORRC_FILE" <<EOF
SocksPort $SOCKS_PORT
ControlPort $CONTROL_PORT
CookieAuthentication 0
MaxCircuitDirtiness 10
NewCircuitPeriod 10
DataDirectory $TOR_DATA
Log notice file $TOR_LOG
EOF

    ok "torrc লেখা হয়েছে"
}

# ---------- Port check ----------
port_open() {
    local port="$1"
    # Termux-এ nc নেই, তাই /dev/tcp ব্যবহার করছি (bash builtin)
    (echo > /dev/tcp/127.0.0.1/"$port") >/dev/null 2>&1
    return $?
}

# ---------- Tor চালু ----------
start_tor() {
    # আগে থেকে চললে বন্ধ করি
    pkill -f "tor.*$SOCKS_PORT" >/dev/null 2>&1
    sleep 1

    log "Tor চালু করা হচ্ছে..."
    tor -f "$TORRC_FILE" >/dev/null 2>&1 &
    TOR_PID=$!
    echo "$TOR_PID" > "$HOME/.tor_pid"

    # SOCKS port-এর জন্য অপেক্ষা (max 60s)
    local i=0
    while [ $i -lt 60 ]; do
        if port_open "$SOCKS_PORT"; then
            ok "Tor SOCKS port $SOCKS_PORT চালু (PID=$TOR_PID)"
            return 0
        fi
        sleep 1
        i=$((i+1))
        printf "\r${C2}[*]${RST} Tor bootstrap... ${C4}%2ds${RST}" "$i"
    done
    echo
    err "Tor SOCKS port খুলতে ব্যর্থ"
    return 1
}

# ---------- IP আনা ----------
get_ip() {
    curl -s --socks5-hostname 127.0.0.1:$SOCKS_PORT \
         --max-time 12 https://api.ipify.org 2>/dev/null
}

# ---------- IP rotate ----------
rotate_ip() {
    # ControlPort-এ SIGNAL NEWNYM পাঠাই
    exec 3<>/dev/tcp/127.0.0.1/$CONTROL_PORT 2>/dev/null || return 1
    printf 'AUTHENTICATE\r\n' >&3
    sleep 0.2
    printf 'SIGNAL NEWNYM\r\n' >&3
    sleep 0.3
    printf 'QUIT\r\n' >&3
    exec 3<&-
    exec 3>&-
    return 0
}

# ---------- Main rotation loop ----------
rotation_loop() {
    echo
    log "Rotation চালু — প্রতি ${C4}${ROTATE_INTERVAL}s${RST} পর পর নতুন IP"
    echo

    local first=1
    local count=0
    local last_ip=""

    while true; do
        if [ $first -eq 1 ]; then
            first=0
            IP=$(get_ip)
            if [ -n "$IP" ]; then
                box "$C3" "INITIAL IP" "🌐  $IP"
                last_ip="$IP"
            else
                box "$C5" "ERROR" "IP আনা যায়নি"
            fi
            sleep "$ROTATE_INTERVAL"
            continue
        fi

        rotate_ip
        sleep 2.5

        IP=$(get_ip)
        count=$((count+1))

        if [ -n "$IP" ] && [ "$IP" != "$last_ip" ]; then
            box "$C6" "NEW IP #$count" "🌐  $IP"
            last_ip="$IP"
        else
            # Retry
            rotate_ip
            sleep 2
            IP2=$(get_ip)
            if [ -n "$IP2" ] && [ "$IP2" != "$last_ip" ]; then
                box "$C6" "NEW IP #$count" "🌐  $IP2"
                last_ip="$IP2"
            else
                box "$C7" "SAME IP #$count" "🌐  ${IP2:-timeout}"
            fi
        fi

        sleep "$ROTATE_INTERVAL"
    done
}

# ---------- Cleanup on exit ----------
cleanup() {
    echo
    warn "থামানো হচ্ছে..."
    if [ -f "$HOME/.tor_pid" ]; then
        local pid
        pid=$(cat "$HOME/.tor_pid")
        kill "$pid" >/dev/null 2>&1
        rm -f "$HOME/.tor_pid"
    fi
    pkill -f "tor.*$SOCKS_PORT" >/dev/null 2>&1
    ok "Tor বন্ধ হয়েছে। বিদায় 👋"
    exit 0
}
trap cleanup INT TERM

# ---------- Main ----------
main() {
    banner
    check_termux
    install_pkgs
    write_torrc

    if ! start_tor; then
        err "Tor চালু করা যায়নি — exit"
        exit 1
    fi

    # ControlPort verify
    if port_open "$CONTROL_PORT"; then
        ok "Control port $CONTROL_PORT চালু — IP rotation সক্রিয়"
    else
        warn "Control port $CONTROL_PORT বন্ধ — rotation কাজ নাও করতে পারে"
    fi

    rotation_loop
}

main
