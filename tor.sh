#!/data/data/com.termux/files/usr/bin/bash
# =============================================================================
#  TERMUX GLOBAL TOR FIX  —  One-time setup
#  যেকোনো ফোল্ডার থেকে রান করুন। এরপর যেকোনো v.py চলবে, timeout আসবে না।
# =============================================================================

RST=$'\033[0m'; BOLD=$'\033[1m'
C1=$'\033[38;5;201m'; C2=$'\033[38;5;51m'
C3=$'\033[38;5;82m';  C4=$'\033[38;5;226m'
C5=$'\033[38;5;196m'; C6=$'\033[38;5;208m'

SOCKS_PORT=9050
CONTROL_PORT=9051
TORRC_DIR="$HOME/.tor"
TORRC_FILE="$TORRC_DIR/torrc"
TOR_DATA="$HOME/.tor_data"
TOR_LOG="$HOME/.tor_log"
TOR_PIDFILE="$HOME/.tor_pid"
MARKER="# >>> ARIYAN-TOR-GLOBAL-FIX >>>"
ENDMARK="# <<< ARIYAN-TOR-GLOBAL-FIX <<<"

log()  { printf "%s[*]%s %s\n" "$C2" "$RST" "$*"; }
ok()   { printf "%s[✓]%s %s\n" "$C3" "$RST" "$*"; }
warn() { printf "%s[!]%s %s\n" "$C4" "$RST" "$*"; }
err()  { printf "%s[✗]%s %s\n" "$C5" "$RST" "$*"; }

banner() {
    clear
    printf "%s%s\n" "$C1" "$BOLD"
    cat <<'EOF'
   ░█████╗░██████╗░██╗██╗░░░██╗░█████╗░███╗░░██╗
   ██╔══██╗██╔══██╗██║╚██╗░██╔╝██╔══██╗████╗░██║
   ███████║██████╔╝██║░╚████╔╝░███████║██╔██╗██║
   ██╔══██║██╔══██╗██║░░╚██╔╝░░██╔══██║██║╚████║
   ██║░░██║██║░░██║██║░░░██║░░░██║░░██║██║░╚███║
   ╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚══╝
EOF
    printf "%s" "$RST"
    printf "%s%s   ░ TERMUX GLOBAL TOR FIX  (যেকোনো ফোল্ডার থেকে রান করুন) ░%s\n\n" \
        "$C2" "$BOLD" "$RST"
}

port_open() { (exec 3<>/dev/tcp/127.0.0.1/"$1") >/dev/null 2>&1; }

# -----------------------------------------------------------------------------
# 1) প্যাকেজ + python module global install
# -----------------------------------------------------------------------------
install_pkgs() {
    log "STEP 1/6 — প্যাকেজ + Python modules"

    local need=()
    command -v tor    >/dev/null 2>&1 || need+=("tor")
    command -v python >/dev/null 2>&1 || need+=("python")
    command -v curl   >/dev/null 2>&1 || need+=("curl")
    command -v pip    >/dev/null 2>&1 || need+=("python-pip")
    command -v nano   >/dev/null 2>&1 || need+=("nano")

    if [ ${#need[@]} -gt 0 ]; then
        warn "ইনস্টল হবে: ${need[*]}"
        pkg update -y >/dev/null 2>&1
        for p in "${need[@]}"; do
            pkg install -y "$p" >/dev/null 2>&1
        done
    fi

    # Python modules (global — যেকোনো ফোল্ডারের যেকোনো স্ক্রিপ্টে কাজ করবে)
    log "Python modules install/verify..."
    pip install --upgrade pip setuptools wheel >/dev/null 2>&1

    local mods=(pycryptodome requests colorama urllib3 charset-normalizer idna certifi)
    for m in "${mods[@]}"; do
        if ! python -c "import ${m//-/_}" >/dev/null 2>&1; then
            log "  → pip install $m"
            pip install --quiet "$m" >/dev/null 2>&1
        fi
    done

    command -v tor    >/dev/null 2>&1 || { err "tor install fail"; exit 1; }
    command -v python >/dev/null 2>&1 || { err "python install fail"; exit 1; }
    ok "সব প্যাকেজ + module ready"
}

# -----------------------------------------------------------------------------
# 2) torrc — global & bootstrap-friendly
# -----------------------------------------------------------------------------
write_torrc() {
    log "STEP 2/6 — global torrc → $TORRC_FILE"
    mkdir -p "$TORRC_DIR" "$TOR_DATA"
    [ -f "$TORRC_FILE" ] && cp "$TORRC_FILE" "$TORRC_FILE.bak.$(date +%s)" 2>/dev/null

    cat > "$TORRC_FILE" <<EOF
SocksPort 127.0.0.1:$SOCKS_PORT
ControlPort 127.0.0.1:$CONTROL_PORT
CookieAuthentication 0
DataDirectory $TOR_DATA
Log notice file $TOR_LOG
ClientOnly 1
MaxCircuitDirtiness 60
NewCircuitPeriod 30
AvoidDiskWrites 0
EOF
    ok "torrc লেখা হয়েছে"
}

# -----------------------------------------------------------------------------
# 3) একবার bootstrap cache তৈরি (ভবিষ্যতে ৫-১০s-এ ready হবে)
# -----------------------------------------------------------------------------
prime_bootstrap() {
    log "STEP 3/6 — Tor bootstrap cache তৈরি (একবারই লাগে, ৩০-১২০s)"

    ps -eo pid,args 2>/dev/null | grep -E '(^|/)tor( |$)' | grep -v grep \
        | awk '{print $1}' | xargs -r kill -9 2>/dev/null
    sleep 1

    : > "$TOR_LOG" 2>/dev/null
    tor -f "$TORRC_FILE" >/dev/null 2>&1 &
    local pid=$!

    local i=0 last_pct=0
    while [ $i -lt 180 ]; do
        if [ -s "$TOR_LOG" ]; then
            local pct
            pct=$(grep -oE 'Bootstrapped [0-9]+' "$TOR_LOG" 2>/dev/null \
                  | tail -n1 | grep -oE '[0-9]+')
            [ -n "$pct" ] && [ "$pct" -gt "$last_pct" ] && last_pct=$pct
        fi

        if port_open "$SOCKS_PORT" && port_open "$CONTROL_PORT"; then
            printf "\r%s[*]%s Bootstrap: %s%d%%%s              \n" \
                "$C2" "$RST" "$C3" "$last_pct" "$RST"
            ok "Tor ready (PID=$pid) — cache সংরক্ষিত"
            kill "$pid" >/dev/null 2>&1
            sleep 1
            return 0
        fi

        printf "\r%s[*]%s Bootstrap: %s%d%%%s [%ds/180s]" \
            "$C2" "$RST" "$C6" "$last_pct" "$RST" "$i"
        sleep 2
        i=$((i+2))
    done
    echo
    kill "$pid" >/dev/null 2>&1

    if grep -q "Bootstrapped 100%" "$TOR_LOG" 2>/dev/null; then
        ok "Log-এ 100% bootstrap পাওয়া গেছে"
        return 0
    fi
    warn "সম্পূর্ণ bootstrap হয়নি — cache তবুও তৈরি হয়েছে"
    return 0
}

# -----------------------------------------------------------------------------
# 4) helper script: tor_up.sh (auto-start tor, reusable)
# -----------------------------------------------------------------------------
install_tor_up_helper() {
    log "STEP 4/6 — helper: $PREFIX/bin/tor_up"

    cat > "$PREFIX/bin/tor_up" <<'TORUP'
#!/data/data/com.termux/files/usr/bin/bash
# Tor আগে থেকে চললে skip, নাহলে চালু করে wait
TORRC="$HOME/.tor/torrc"
LOG="$HOME/.tor_log"
PIDFILE="$HOME/.tor_pid"

port_open() { (exec 3<>/dev/tcp/127.0.0.1/"$1") >/dev/null 2>&1; }

if port_open 9050 && port_open 9051; then
    exit 0
fi

# পুরনো tor বন্ধ
ps -eo pid,args 2>/dev/null | grep -E '(^|/)tor( |$)' | grep -v grep \
    | awk '{print $1}' | xargs -r kill -9 2>/dev/null
sleep 1

: > "$LOG" 2>/dev/null
tor -f "$TORRC" >/dev/null 2>&1 &
echo $! > "$PIDFILE"

i=0
while [ $i -lt 180 ]; do
    if port_open 9050 && port_open 9051; then
        exit 0
    fi
    sleep 2
    i=$((i+2))
done
exit 1
TORUP
    chmod +x "$PREFIX/bin/tor_up"
    ok "tor_up helper ইনস্টল: $PREFIX/bin/tor_up"
}

# -----------------------------------------------------------------------------
# 5) ~/.bashrc — auto-start Tor + python wrapper
# -----------------------------------------------------------------------------
install_bashrc_hook() {
    log "STEP 5/6 — ~/.bashrc-এ auto-start hook"

    local BR="$HOME/.bashrc"
    touch "$BR"

    # পুরনো block সরাও (re-run safe)
    if grep -q "$MARKER" "$BR"; then
        # marker থেকে endmark পর্যন্ত কাটো
        python - "$BR" "$MARKER" "$ENDMARK" <<'PYEOF'
import sys, re
path, m, e = sys.argv[1], sys.argv[2], sys.argv[3]
with open(path, 'r', encoding='utf-8') as f:
    txt = f.read()
txt = re.sub(re.escape(m) + r'.*?' + re.escape(e) + r'\n?', '', txt, flags=re.S)
with open(path, 'w', encoding='utf-8') as f:
    f.write(txt)
PYEOF
    fi

    cat >> "$BR" <<BASHRC

$MARKER
# ── Termux-এ প্রতি নতুন session-এ Tor auto-start ──
if [ -z "\$ARIYAN_TOR_STARTED" ] && command -v tor >/dev/null 2>&1; then
    export ARIYAN_TOR_STARTED=1
    # শুধু interactive shell-এ
    case "\$-" in
        *i*)
            if ! (exec 3<>/dev/tcp/127.0.0.1/9050) 2>/dev/null; then
                (tor -f "\$HOME/.tor/torrc" >/dev/null 2>&1 &) >/dev/null 2>&1
            fi
            ;;
    esac
fi

# ── python wrapper: চালানোর আগে Tor verify ──
python() {
    local first_arg="\$1"
    case "\$first_arg" in
        *.py)
            # Tor চলছে কিনা check; না থাকলে tor_up (max 180s wait)
            if ! (exec 3<>/dev/tcp/127.0.0.1/9050) 2>/dev/null; then
                if command -v tor_up >/dev/null 2>&1; then
                    printf '\033[38;5;51m[*]\033[0m Tor চালু হচ্ছে...\n'
                    tor_up
                fi
            fi
            ;;
    esac
    command python "\$@"
}
$ENDMARK
BASHRC

    ok "~/.bashrc-এ hook যোগ করা হয়েছে"
    warn "active shell-এ apply করতে: source ~/.bashrc"
}

# -----------------------------------------------------------------------------
# 6) verify
# -----------------------------------------------------------------------------
verify() {
    log "STEP 6/6 — verify"

    [ -f "$TORRC_FILE" ] && ok "torrc: $TORRC_FILE"
    [ -d "$TOR_DATA" ]   && ok "data cache: $TOR_DATA"
    [ -x "$PREFIX/bin/tor_up" ] && ok "tor_up helper executable"
    grep -q "$MARKER" "$HOME/.bashrc" 2>/dev/null && ok "~/.bashrc hook আছে"

    # tor binary
    if command -v tor >/dev/null 2>&1; then
        ok "tor binary: $(command -v tor)"
    fi

    # python modules
    for m in Crypto requests colorama; do
        python -c "import $m" >/dev/null 2>&1 && ok "python module: $m"
    done
}

# -----------------------------------------------------------------------------
print_summary() {
    echo
    printf "%s%s╔════════════════════════════════════════════════════╗%s\n" "$C3" "$BOLD" "$RST"
    printf "%s%s║        ✅  TERMUX  GLOBALLY  FIXED                 ║%s\n" "$C3" "$BOLD" "$RST"
    printf "%s%s╚════════════════════════════════════════════════════╝%s\n" "$C3" "$BOLD" "$RST"
    echo
    printf "%sএখন কী করতে হবে:%s\n" "$C4$BOLD" "$RST"
    echo
    printf "  %s1.%s একটি নতুন Terminal খুলুন (অথবা চালান: %ssource ~/.bashrc%s)\n" \
        "$C3" "$RST" "$C6" "$RST"
    echo
    printf "  %s2.%s যেকোনো ফোল্ডারে যান:\n" "$C3" "$RST"
    printf "        %scd /storage/emulated/0/যেকোনো-ফোল্ডার%s\n" "$C6" "$RST"
    echo
    printf "  %s3.%s যেকোনো v.py চালান:\n" "$C3" "$RST"
    printf "        %spython v.py%s\n" "$C6$BOLD" "$RST"
    echo
    printf "%sএখন Termux যা করবে:%s\n" "$C4$BOLD" "$RST"
    printf "  %s•%s Termux খোলার সাথে সাথে Tor auto-start হবে\n" "$C2" "$RST"
    printf "  %s•%s যেকোনো .py চালালে Tor আগেই ready থাকবে\n" "$C2" "$RST"
    printf "  %s•%s Python modules সব ফোল্ডারে কাজ করবে\n" "$C2" "$RST"
    printf "  %s•%s bootstrap cache থাকায় %s৫-১০ সেকেন্ডে%s ready হবে\n" "$C2" "$RST" "$C3" "$RST"
    echo
}

# -----------------------------------------------------------------------------
main() {
    banner
    install_pkgs
    write_torrc
    prime_bootstrap
    install_tor_up_helper
    install_bashrc_hook
    verify
    print_summary
}

main
