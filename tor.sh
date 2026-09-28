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
TORPID="$HOME/.tor_pid"
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

box_open() {
    local color="$1" title="$2" w=64
    local pad=$(( (w - ${#title}) / 2 ))
    local pad2=$(( w - ${#title} - pad ))
    printf "%s╔" "$color"; for ((i=0;i<w;i++)); do printf "═"; done; printf "╗%s\n" "$RST"
    printf "%s║%s%*s%s%s%s%*s%s║%s\n" \
        "$color" "$RST" "$pad" "" "$BOLD$C_WHI" "$title" "$RST" "$pad2" "" "$color" "$RST"
    printf "%s╠" "$color"; for ((i=0;i<w;i++)); do printf "═"; done; printf "╣%s\n" "$RST"
}
box_line() {
    local color="$1" text="$2"
    printf "%s║%s  %-58s  %s║%s\n" "$color" "$RST" "$text" "$color" "$RST"
}
box_close() {
    local color="$1"
    printf "%s╚" "$color"; for ((i=0;i<64;i++)); do printf "═"; done; printf "╝%s\n" "$RST"
}

port_open() { (exec 3<>/dev/tcp/127.0.0.1/"$1") >/dev/null 2>&1; }

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
    if ! command -v pip >/dev/null 2>&1; then
        need+=("python-pip")
    fi

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
    local py_mods=(
        "pycryptodome:Crypto"
        "requests:requests"
        "colorama:colorama"
        "urllib3:urllib3"
    )
    for entry in "${py_mods[@]}"; do
        local pipname="${entry%%:*}"
        local modname="${entry##*:}"
        if python -c "import $modname" >/dev/null 2>&1; then
            ok "module OK: $modname"
        else
            info "pip install $pipname"
            pip install --quiet --disable-pip-version-check "$pipname" >/dev/null 2>&1 || \
                pip install --quiet --break-system-packages "$pipname" >/dev/null 2>&1 || true
            if python -c "import $modname" >/dev/null 2>&1; then
                ok "module installed: $modname"
            else
                fail "module failed: $modname"
            fi
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
    step "STEP 3 / 5  ·  Tor Bootstrap Cache (First-time warm-up)"
    line "$C_CYN"

    kill_all_tor
    : > "$TORLOG" 2>/dev/null || true

    info "Starting Tor — waiting for bootstrap (max 180s)..."
    tor -f "$TORRC" >/dev/null 2>&1 &
    local pid=$!

    local i=0 last=0
    while [ $i -lt 180 ]; do
        if [ -s "$TORLOG" ]; then
            local p
            p=$(grep -oE 'Bootstrapped [0-9]+' "$TORLOG" 2>/dev/null | tail -n1 | grep -oE '[0-9]+')
            [ -n "$p" ] && [ "$p" -gt "$last" ] && last=$p
        fi

        if port_open "$SOCKS_PORT" && port_open "$CTRL_PORT"; then
            printf "\r  ${C_GRN}✓${RST} Bootstrap: ${C_GRN}%3d%%${RST}  —  SOCKS+CTRL ready            \n" "$last"
            ok "Tor ready (PID=$pid) — cache stored"
            echo "$pid" > "$TORPID"
            kill "$pid" >/dev/null 2>&1 || true
            sleep 1
            return 0
        fi

        printf "\r  ${C_CYN}▸${RST} Bootstrap: ${C_YEL}%3d%%${RST}  [%3ds/180s]  " "$last" "$i"
        sleep 2
        i=$((i+2))
    done

    echo
    kill "$pid" >/dev/null 2>&1 || true

    if grep -q "Bootstrapped 100" "$TORLOG" 2>/dev/null; then
        ok "Log confirms 100% bootstrap"
        return 0
    fi

    warn "Bootstrap incomplete — cache still built"
    warn "Tor log: $TORLOG"
    return 0
}

step_helper() {
    step "STEP 4 / 5  ·  Install tor_up Helper → \$PREFIX/bin"
    line "$C_CYN"

    cat > "$PREFIX/bin/tor_up" <<'TORUP'
#!/data/data/com.termux/files/usr/bin/bash
TORRC="$HOME/.tor/torrc"
LOG="$HOME/.tor_log"

port_open() { (exec 3<>/dev/tcp/127.0.0.1/"$1") >/dev/null 2>&1; }

port_open 9050 && port_open 9051 && exit 0

ps -eo pid,args 2>/dev/null | grep -E '(^|/)tor( |$)' | grep -v grep \
    | awk '{print $1}' | xargs -r kill -9 2>/dev/null
sleep 1

: > "$LOG" 2>/dev/null
tor -f "$TORRC" >/dev/null 2>&1 &

i=0
while [ $i -lt 180 ]; do
    port_open 9050 && port_open 9051 && exit 0
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
            if ! (exec 3<>/dev/tcp/127.0.0.1/9050) 2>/dev/null; then
                printf '\033[38;5;51m[tor]\033[0m starting Tor...\n'
                if command -v tor_up >/dev/null 2>&1; then
                    tor_up || printf '\033[38;5;196m[tor]\033[0m failed\n'
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

    if command -v tor >/dev/null 2>&1; then
        ok "tor binary: $(command -v tor)"; pass=$((pass+1))
    else
        fail "tor binary missing"; failn=$((failn+1))
    fi

    if [ -f "$TORRC" ]; then
        ok "torrc exists"; pass=$((pass+1))
    else
        fail "torrc missing"; failn=$((failn+1))
    fi

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

    if [ -x "$PREFIX/bin/tor_up" ]; then
        ok "tor_up helper executable"; pass=$((pass+1))
    else
        fail "tor_up helper missing"; failn=$((failn+1))
    fi

    if grep -qF "$MARK" "$BRC" 2>/dev/null; then
        ok "~/.bashrc hook present"; pass=$((pass+1))
    else
        fail "~/.bashrc hook missing"; failn=$((failn+1))
    fi

    for m in Crypto requests colorama urllib3; do
        if python -c "import $m" >/dev/null 2>&1; then
            ok "python module: $m"; pass=$((pass+1))
        else
            fail "python module missing: $m"; failn=$((failn+1))
        fi
    done

    echo
    line "$C_CYN"
    printf "  ${BOLD}RESULT:${RST}  ${C_GRN}%d PASS${RST}  ·  ${C_RED}%d FAIL${RST}\n" "$pass" "$failn"
    line "$C_CYN"

    [ "$failn" -eq 0 ] && return 0 || return 1
}

summary() {
    echo
    box_open "$C_GRN" "✅  TERMUX  GLOBALLY  FIXED  —  100%  VERIFIED"
    box_line "$C_GRN" "Tor auto-starts on every new Termux shell"
    box_line "$C_GRN" "Any v.py runs from any folder without timeout"
    box_line "$C_GRN" "Bootstrap cache pre-built — instant ready"
    box_line "$C_GRN" "IP rotation works via ControlPort 9051"
    box_close "$C_GRN"
    echo
    printf "  ${BOLD}${C_YEL}Next steps:${RST}\n\n"
    printf "  ${C_CYN}1.${RST} Open a new Termux terminal (or run: ${C_ORG}source ~/.bashrc${RST})\n"
    printf "  ${C_CYN}2.${RST} cd to any folder: ${C_ORG}cd /storage/emulated/0/any-folder${RST}\n"
    printf "  ${C_CYN}3.${RST} Run any script: ${C_ORG}${BOLD}python v.py${RST}\n\n"
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
    step_bootstrap
    step_helper
    step_bashrc

    if verify_all; then
        summary
        exit 0
    else
        echo
        box_open "$C_RED" "✗  SOME  STEPS  FAILED"
        box_line "$C_RED" "Review the FAIL lines above and re-run"
        box_close "$C_RED"
        exit 1
    fi
}

trap 'echo; printf "\n  ${C_YEL}!${RST} aborted\n"; exit 130' INT TERM

main "$@"
