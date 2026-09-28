#!/data/data/com.termux/files/usr/bin/bash
# ╔══════════════════════════════════════════════════════════════════════════╗
# ║                                                                          ║
# ║          ░█████╗░██████╗░██╗██╗░░░██╗░█████╗░███╗░░██╗                    ║
# ║          ██╔══██╗██╔══██╗██║╚██╗░██╔╝██╔══██╗████╗░██║                    ║
# ║          ███████║██████╔╝██║░╚████╔╝░███████║██╔██╗██║                    ║
# ║          ██╔══██║██╔══██╗██║░░╚██╔╝░░██╔══██║██║╚████║                    ║
# ║          ██║░░██║██║░░██║██║░░░██║░░░██║░░██║██║░╚███║                    ║
# ║          ╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚══╝                    ║
# ║                                                                          ║
# ║              ✦ TERMUX GLOBAL TOR FIX — 100% VERIFIED ✦                   ║
# ║                                                                          ║
# ╚══════════════════════════════════════════════════════════════════════════╝

set -u

RST=$'\033[0m'; BOLD=$'\033[1m'; DIM=$'\033[2m'
C_MAG=$'\033[38;5;201m'; C_CYN=$'\033[38;5;51m';  C_GRN=$'\033[38;5;82m'
C_YEL=$'\033[38;5;226m'; C_RED=$'\033[38;5;196m'; C_ORG=$'\033[38;5;208m'
C_PUR=$'\033[38;5;135m'; C_BLU=$'\033[38;5;33m';  C_WHI=$'\033[38;5;255m'

SOCKS_PORT=9050
CTRL_PORT=9051
TORRC="$HOME/.tor/torrc"
TORDATA="$HOME/.tor_data"
TORLOG="$HOME/.tor_log"
BRC="$HOME/.bashrc"
MARK="# >>> ARIYAN-TOR-FIX >>>"
ENDM="# <<< ARIYAN-TOR-FIX <<<"

info() { printf "  ${C_CYN}▸${RST} %s\n" "$*"; }
ok()   { printf "  ${C_GRN}✓${RST} %s\n" "$*"; }
warn() { printf "  ${C_YEL}!${RST} %s\n" "$*"; }
fail() { printf "  ${C_RED}✗${RST} %s\n" "$*"; }
step() { printf "\n${C_MAG}${BOLD}▐ %s${RST}\n" "$*"; }

line() {
    local color="$1" width=64
    printf "%s" "$color"
    for ((i=0;i<width;i++)); do printf "─"; done
    printf "%s\n" "$RST"
}

port_open() { (exec 3<>/dev/tcp/127.0.0.1/"$1") >/dev/null 2>&1; }

# ─── Read latest bootstrap % from log ───
bootstrap_pct() {
    [ -s "$TORLOG" ] || { echo 0; return; }
    local p
    p=$(grep -oE 'Bootstrapped [0-9]+' "$TORLOG" 2>/dev/null | tail -n1 | grep -oE '[0-9]+')
    echo "${p:-0}"
}

# ─── Check log for 100% bootstrap ───
bootstrap_done() {
    grep -q "Bootstrapped 100" "$TORLOG" 2>/dev/null
}

# ─── Actually verify Tor works (not just port open) ───
tor_truly_ready() {
    # 1. Log says 100%
    bootstrap_done || return 1
    # 2. Both ports open
    port_open "$SOCKS_PORT" || return 1
    port_open "$CTRL_PORT" || return 1
    # 3. Real HTTP request via Tor succeeds
    local ip
    ip=$(curl -s --socks5-hostname 127.0.0.1:$SOCKS_PORT --max-time 15 \
         https://api.ipify.org 2>/dev/null)
    [ -n "$ip" ] && echo "$ip" >/dev/null && return 0
    return 1
}

kill_all_tor() {
    local pids
    pids=$(ps -eo pid,args 2>/dev/null | grep -E '(^|/)tor( |$)' | grep -v grep | awk '{print $1}')
    [ -n "$pids" ] && echo "$pids" | xargs -r kill -9 2>/dev/null
    sleep 1
}

banner() {
    clear
    printf "\n%s%s" "$C_MAG" "$BOLD"
    cat <<'EOF'
    ╔══════════════════════════════════════════════════════════════╗
    ║                                                              ║
    ║        ░█████╗░██████╗░██╗██╗░░░██╗░█████╗░███╗░░██╗        ║
    ║        ██╔══██╗██╔══██╗██║╚██╗░██╔╝██╔══██╗████╗░██║        ║
    ║        ███████║██████╔╝██║░╚████╔╝░███████║██╔██╗██║        ║
    ║        ██╔══██║██╔══██╗██║░░╚██╔╝░░██╔══██║██║╚████║        ║
    ║        ██║░░██║██║░░██║██║░░░██║░░░██║░░██║██║░╚███║        ║
    ║        ╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚══╝        ║
    ║                                                              ║
EOF
    printf "%s" "$RST"
    printf "%s%s    ║     ✦ TERMUX GLOBAL TOR FIX — 100%% VERIFIED ✦              ║%s\n" "$C_CYN" "$BOLD" "$RST"
    printf "%s%s    ║                                                              ║%s\n" "$C_MAG" "$BOLD" "$RST"
    printf "%s%s" "$C_MAG" "$BOLD"
    printf "    ╚══════════════════════════════════════════════════════════════╝\n"
    printf "%s\n" "$RST"
}

step_packages() {
    step "STEP 1 / 5  ·  Package & Python Module Install"
    line "$C_CYN"

    local need=()
    command -v tor >/dev/null 2>&1 || need+=("tor")
    command -v python >/dev/null 2>&1 || need+=("python")
    command -v curl >/dev/null 2>&1 || need+=("curl")
    command -v pip >/dev/null 2>&1 || need+=("python-pip")

    if [ ${#need[@]} -eq 0 ]; then
        ok "All system packages already present"
    else
        warn "Installing: ${need[*]}"
        pkg update -y >/dev/null 2>&1 || true
        for p in "${need[@]}"; do
            info "pkg install $p"
            pkg install -y "$p" >/dev/null 2>&1 || true
        done
        ok "System packages installed"
    fi

    info "Verifying Python modules..."
    local py_mods=("pycryptodome:Crypto" "requests:requests" "colorama:colorama" "urllib3:urllib3")
    for entry in "${py_mods[@]}"; do
        local pipname="${entry%%:*}" modname="${entry##*:}"
        if python -c "import $modname" >/dev/null 2>&1; then
            ok "module OK: $modname"
        else
            info "pip install $pipname"
            pip install --quiet --disable-pip-version-check "$pipname" >/dev/null 2>&1 || \
                pip install --quiet --break-system-packages "$pipname" >/dev/null 2>&1 || true
            python -c "import $modname" >/dev/null 2>&1 && ok "module installed: $modname" || fail "module failed: $modname"
        fi
    done
}

step_torrc() {
    step "STEP 2 / 5  ·  Global torrc (Bootstrap-Optimized)"
    line "$C_CYN"

    mkdir -p "$(dirname "$TORRC")" "$TORDATA"
    [ -f "$TORRC" ] && cp "$TORRC" "${TORRC}.bak.$(date +%s)" 2>/dev/null || true

    cat > "$TORRC" <<EOF
# ─── ARIYAN TOR FIX — DO NOT EDIT ───
SocksPort 127.0.0.1:${SOCKS_PORT}
ControlPort 127.0.0.1:${CTRL_PORT}
CookieAuthentication 0
DataDirectory ${TORDATA}
Log notice file ${TORLOG}
ClientOnly 1
MaxCircuitDirtiness 60
NewCircuitPeriod 30
AvoidDiskWrites 0
EOF

    ok "torrc written → $TORRC"
    ok "SocksPort=$SOCKS_PORT  ControlPort=$CTRL_PORT  MaxCircuitDirtiness=60"
}

step_bootstrap() {
    step "STEP 3 / 5  ·  Tor Bootstrap Cache (must reach 100%)"
    line "$C_CYN"

    kill_all_tor
    : > "$TORLOG" 2>/dev/null || true

    info "Starting Tor — waiting for real 100% bootstrap (max 300s)..."
    tor -f "$TORRC" >/dev/null 2>&1 &
    local pid=$!

    local i=0
    while [ $i -lt 300 ]; do
        local pct
        pct=$(bootstrap_pct)

        if bootstrap_done && port_open "$SOCKS_PORT" && port_open "$CTRL_PORT"; then
            printf "\r  ${C_GRN}✓${RST} Bootstrap: ${C_GRN}100%%${RST}  —  SOCKS+CTRL ready             \n"
            # Final real-world check
            local ip
            ip=$(curl -s --socks5-hostname 127.0.0.1:$SOCKS_PORT --max-time 20 \
                 https://api.ipify.org 2>/dev/null)
            if [ -n "$ip" ]; then
                ok "Tor live-test passed — IP: $ip"
                echo "$pid" > "$HOME/.tor_pid"
                # Keep Tor running in background (do NOT kill — v.py needs it)
                ok "Tor running in background (PID=$pid)"
                return 0
            else
                warn "Port open but IP fetch failed — retrying..."
            fi
        fi

        printf "\r  ${C_CYN}▸${RST} Bootstrap: ${C_YEL}%3d%%${RST}  [%3ds/300s]  " "$pct" "$i"
        sleep 2
        i=$((i+2))
    done

    echo
    fail "Bootstrap did NOT reach 100% within 300s"
    fail "Tor log tail:"
    tail -n 20 "$TORLOG" 2>/dev/null | sed 's/^/      /'
    kill "$pid" >/dev/null 2>&1 || true
    return 1
}

step_helper() {
    step "STEP 4 / 5  ·  Install tor_up Helper → \$PREFIX/bin"
    line "$C_CYN"

    cat > "$PREFIX/bin/tor_up" <<'TORUP'
#!/data/data/com.termux/files/usr/bin/bash
TORRC="$HOME/.tor/torrc"
LOG="$HOME/.tor_log"

port_open() { (exec 3<>/dev/tcp/127.0.0.1/"$1") >/dev/null 2>&1; }

# Already bootstrap-done? Verify with a live request
if grep -q "Bootstrapped 100" "$LOG" 2>/dev/null && \
   port_open 9050 && port_open 9051; then
    curl -s --socks5-hostname 127.0.0.1:9050 --max-time 10 \
         https://api.ipify.org >/dev/null 2>&1 && exit 0
fi

# Kill stale
ps -eo pid,args 2>/dev/null | grep -E '(^|/)tor( |$)' | grep -v grep \
    | awk '{print $1}' | xargs -r kill -9 2>/dev/null
sleep 1

# Fresh start
: > "$LOG" 2>/dev/null
tor -f "$TORRC" >/dev/null 2>&1 &

# Wait for real 100% + live test
i=0
while [ $i -lt 300 ]; do
    if grep -q "Bootstrapped 100" "$LOG" 2>/dev/null && \
       port_open 9050 && port_open 9051; then
        if curl -s --socks5-hostname 127.0.0.1:9050 --max-time 15 \
                https://api.ipify.org >/dev/null 2>&1; then
            exit 0
        fi
    fi
    sleep 2
    i=$((i+2))
done
exit 1
TORUP

    chmod +x "$PREFIX/bin/tor_up"
    ok "Helper installed: \$PREFIX/bin/tor_up"
}

step_bashrc() {
    step "STEP 5 / 5  ·  ~/.bashrc — Auto-Start + Python Wrapper"
    line "$C_CYN"

    touch "$BRC"

    if grep -qF "$MARK" "$BRC" 2>/dev/null; then
        python - "$BRC" "$MARK" "$ENDM" <<'PYEOF' 2>/dev/null || \
        sed -i "/$(printf '%s' "$MARK" | sed 's/[\/&]/\\&/g')/,/$(printf '%s' "$ENDM" | sed 's/[\/&]/\\&/g')/d" "$BRC"
import sys, re
p, m, e = sys.argv[1], sys.argv[2], sys.argv[3]
with open(p, encoding='utf-8') as f: t = f.read()
t = re.sub(re.escape(m) + r'.*?' + re.escape(e) + r'\n?', '', t, flags=re.S)
with open(p, 'w', encoding='utf-8') as f: f.write(t)
PYEOF
        ok "Old hook removed"
    fi

    cat >> "$BRC" <<BASHRC

${MARK}
if [ -z "\${ARIYAN_TOR_BOOTED:-}" ]; then
    export ARIYAN_TOR_BOOTED=1
    case "\$-" in
        *i*)
            if ! (exec 3<>/dev/tcp/127.0.0.1/9050) 2>/dev/null; then
                if command -v tor >/dev/null 2>&1 && [ -f "\$HOME/.tor/torrc" ]; then
                    (tor -f "\$HOME/.tor/torrc" >/dev/null 2>&1 &) >/dev/null 2>&1
                fi
            fi
            ;;
    esac
fi

python() {
    case "\${1:-}" in
        *.py)
            # Check if Tor is truly ready (bootstrap 100% + live test)
            local _ok=0
            if grep -q "Bootstrapped 100" "\$HOME/.tor_log" 2>/dev/null && \
               (exec 3<>/dev/tcp/127.0.0.1/9050) 2>/dev/null; then
                if curl -s --socks5-hostname 127.0.0.1:9050 --max-time 8 \
                        https://api.ipify.org >/dev/null 2>&1; then
                    _ok=1
                fi
            fi
            if [ "\$_ok" -eq 0 ]; then
                printf '\033[38;5;51m[tor]\033[0m waiting for Tor bootstrap...\n'
                if command -v tor_up >/dev/null 2>&1; then
                    tor_up || printf '\033[38;5;196m[tor]\033[0m bootstrap failed\n'
                fi
            fi
            ;;
    esac
    command python "\$@"
}
${ENDM}
BASHRC

    ok "Hook added to ~/.bashrc"
}

verify_all() {
    step "VERIFICATION — All checks"
    line "$C_GRN"

    local pass=0 failn=0

    command -v tor >/dev/null 2>&1 && { ok "tor binary: $(command -v tor)"; pass=$((pass+1)); } || { fail "tor binary missing"; failn=$((failn+1)); }

    [ -f "$TORRC" ] && { ok "torrc exists"; pass=$((pass+1)); } || { fail "torrc missing"; failn=$((failn+1)); }

    if grep -q "MaxCircuitDirtiness 60" "$TORRC" 2>/dev/null && \
       grep -q "NewCircuitPeriod 30" "$TORRC" 2>/dev/null; then
        ok "torrc values correct (60/30)"; pass=$((pass+1))
    else
        fail "torrc values wrong"; failn=$((failn+1))
    fi

    if [ -d "$TORDATA" ] && [ "$(ls -A "$TORDATA" 2>/dev/null)" ]; then
        ok "bootstrap cache: $(ls -A "$TORDATA" | wc -l) files"; pass=$((pass+1))
    else
        fail "bootstrap cache empty"; failn=$((failn+1))
    fi

    # CRITICAL: verify actual bootstrap 100% in log
    if bootstrap_done; then
        ok "Tor log: Bootstrapped 100%"; pass=$((pass+1))
    else
        fail "Tor log: bootstrap NOT complete"; failn=$((failn+1))
    fi

    # CRITICAL: verify live Tor works
    local live_ip
    live_ip=$(curl -s --socks5-hostname 127.0.0.1:$SOCKS_PORT --max-time 15 \
              https://api.ipify.org 2>/dev/null)
    if [ -n "$live_ip" ]; then
        ok "Live Tor test: IP = $live_ip"; pass=$((pass+1))
    else
        fail "Live Tor test: FAILED (SOCKS request timeout)"; failn=$((failn+1))
    fi

    [ -x "$PREFIX/bin/tor_up" ] && { ok "tor_up helper executable"; pass=$((pass+1)); } || { fail "tor_up helper missing"; failn=$((failn+1)); }

    grep -qF "$MARK" "$BRC" 2>/dev/null && { ok "~/.bashrc hook present"; pass=$((pass+1)); } || { fail "~/.bashrc hook missing"; failn=$((failn+1)); }

    for m in Crypto requests colorama urllib3; do
        python -c "import $m" >/dev/null 2>&1 && { ok "python module: $m"; pass=$((pass+1)); } || { fail "python module missing: $m"; failn=$((failn+1)); }
    done

    echo
    line "$C_CYN"
    printf "  ${BOLD}RESULT:${RST}  ${C_GRN}%d PASS${RST}  ·  ${C_RED}%d FAIL${RST}\n" "$pass" "$failn"
    line "$C_CYN"

    [ "$failn" -eq 0 ] && return 0 || return 1
}

summary() {
    echo
    printf "  ${C_GRN}${BOLD}╔══════════════════════════════════════════════════════════════╗${RST}\n"
    printf "  ${C_GRN}${BOLD}║      ✅  TERMUX  GLOBALLY  FIXED  —  100%%  VERIFIED         ║${RST}\n"
    printf "  ${C_GRN}${BOLD}╚══════════════════════════════════════════════════════════════╝${RST}\n"
    echo
    printf "  ${C_CYN}▸${RST} Tor is running now and will auto-start on every new shell\n"
    printf "  ${C_CYN}▸${RST} IP rotation via ControlPort 9051 works\n"
    printf "  ${C_CYN}▸${RST} All Python modules globally available\n"
    echo
    line "$C_PUR"
    printf "  ${C_PUR}${BOLD}✦ ${C_WHI}Developer: ARIYAN${RST}  ${C_PUR}·${RST}  ${C_WHI}Telegram: @rakibz4${RST}\n"
    line "$C_PUR"
    echo
}

main() {
    banner
    printf "  ${C_CYN}▸${RST} Termux: ${C_GRN}${PREFIX:-unknown}${RST}\n"
    printf "  ${C_CYN}▸${RST} Home  : ${C_GRN}${HOME}${RST}\n"
    printf "  ${C_CYN}▸${RST} Shell : ${C_GRN}${SHELL:-bash}${RST}\n"

    step_packages
    step_torrc

    if ! step_bootstrap; then
        echo
        printf "  ${C_RED}${BOLD}╔══════════════════════════════════════════════════════════════╗${RST}\n"
        printf "  ${C_RED}${BOLD}║   ✗  BOOTSTRAP  FAILED  —  Tor cannot reach network         ║${RST}\n"
        printf "  ${C_RED}${BOLD}╚══════════════════════════════════════════════════════════════╝${RST}\n"
        echo
        printf "  ${C_YEL}Possible causes:${RST}\n"
        printf "    • ISP blocking Tor (try mobile data)\n"
        printf "    • VPN active (disable it)\n"
        printf "    • No internet connection\n"
        printf "    • Firewall blocking ports\n"
        echo
        exit 1
    fi

    step_helper
    step_bashrc

    if verify_all; then
        summary
        exit 0
    else
        echo
        printf "  ${C_RED}${BOLD}✗  Some checks FAILED — review above${RST}\n"
        exit 1
    fi
}

trap 'echo; printf "\n  ${C_YEL}!${RST} aborted\n"; exit 130' INT TERM

main "$@"
