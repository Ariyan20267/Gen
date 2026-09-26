#!/data/data/com.termux/files/usr/bin/bash

# ============================================================
#                 ARIYAN RGB SETUP INSTALLER
#              NO GITHUB • NO EXTRA EXECUTION
# ============================================================

RESET="\033[0m"
BOLD="\033[1m"
DIM="\033[2m"

RED="\033[38;5;196m"
ORANGE="\033[38;5;208m"
YELLOW="\033[38;5;226m"
GREEN="\033[38;5;118m"
CYAN="\033[38;5;51m"
BLUE="\033[38;5;45m"
PURPLE="\033[38;5;93m"
MAGENTA="\033[38;5;201m"
PINK="\033[38;5;198m"
GOLD="\033[38;5;220m"
LIME="\033[38;5;154m"
VIOLET="\033[38;5;129m"
HOT="\033[38;5;212m"

RGB=(
    "$RED"
    "$ORANGE"
    "$YELLOW"
    "$GREEN"
    "$CYAN"
    "$BLUE"
    "$PURPLE"
    "$MAGENTA"
    "$PINK"
    "$GOLD"
    "$LIME"
    "$VIOLET"
    "$HOT"
)

RGB_LEN=${#RGB[@]}

# ============================================================
#                         LOGO
# ============================================================

ARIYAN=(
"        █████╗ ██████╗ ██╗██╗   ██╗ █████╗ ███╗   ██╗"
"       ██╔══██╗██╔══██╗██║╚██╗ ██╔╝██╔══██╗████╗  ██║"
"       ███████║██████╔╝██║ ╚████╔╝ ███████║██╔██╗ ██║"
"       ██╔══██║██╔══██╗██║  ╚██╔╝  ██╔══██║██║╚████║"
"       ██║  ██║██║  ██║██║   ██║   ██║  ██║██║ ╚███║"
"       ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚══╝"
)

# ============================================================
#                       TERMINAL
# ============================================================

hide_cursor() {
    printf "\033[?25l"
}

show_cursor() {
    printf "\033[?25h"
}

cleanup() {
    show_cursor
    rm -f /tmp/ariyan_install_status
    rm -f /tmp/ariyan_install_log
}

trap cleanup EXIT INT TERM

clear
hide_cursor

# ============================================================
#                    RGB LOGO ANIMATION
# ============================================================

logo_animation() {

    for round in {1..8}; do

        clear
        echo ""
        echo ""

        i=0

        for line in "${ARIYAN[@]}"; do
            COLOR="${RGB[$(( (i + round) % RGB_LEN ))]}"
            echo -e "  ${COLOR}${BOLD}${line}${RESET}"
            i=$((i + 1))
        done

        echo ""
        echo -e "  ${RGB[$((round % RGB_LEN))]}${BOLD}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${RESET}"
        echo -e "  ${WHITE}${BOLD}                    A R I Y A N                     ${RESET}"
        echo -e "  ${RGB[$(((round + 6) % RGB_LEN))]}${BOLD}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${RESET}"

        sleep 0.10

    done
}

# ============================================================
#                    GLOW HEADER
# ============================================================

header() {

    local title="$1"

    echo ""
    echo -e "${PURPLE}${BOLD}  ╔════════════════════════════════════════════════════════╗${RESET}"
    echo -e "${CYAN}${BOLD}  ║${RESET}   ${WHITE}${BOLD}${title}${RESET}"
    echo -e "${PURPLE}${BOLD}  ╚════════════════════════════════════════════════════════╝${RESET}"
    echo ""

}

# ============================================================
#                    ANIMATED DOTS
# ============================================================

loading() {

    local TEXT="$1"
    local COUNT="${2:-20}"

    local FRAMES=("⠋" "⠙" "⠹" "⠸" "⠼" "⠴" "⠦" "⠧" "⠇" "⠏")
    local i=0

    while [ "$i" -lt "$COUNT" ]; do

        COLOR="${RGB[$((i % RGB_LEN))]}"
        FRAME="${FRAMES[$((i % ${#FRAMES[@]}))]}"

        printf "\r\033[2K"
        echo -ne "  ${COLOR}${BOLD}${FRAME} ${TEXT}${RESET}"

        sleep 0.08
        i=$((i + 1))

    done

    printf "\r\033[2K"

}

# ============================================================
#                    RGB PROGRESS
# ============================================================

progress_bar() {

    local CURRENT="$1"
    local TOTAL="$2"
    local WIDTH=44

    local FILLED=$((CURRENT * WIDTH / TOTAL))
    local EMPTY=$((WIDTH - FILLED))
    local BAR=""

    for ((i=0; i<FILLED; i++)); do
        COLOR="${RGB[$((i % RGB_LEN))]}"
        BAR="${BAR}${COLOR}${BOLD}█${RESET}"
    done

    for ((i=0; i<EMPTY; i++)); do
        BAR="${BAR}${DIM}░${RESET}"
    done

    local PERCENT=$((CURRENT * 100 / TOTAL))

    echo -e "  ${BAR} ${WHITE}${BOLD}${PERCENT}%${RESET}"

}

# ============================================================
#                       START
# ============================================================

logo_animation

clear

echo ""
echo -e "${CYAN}${BOLD}  ╔════════════════════════════════════════════════════════╗${RESET}"
echo -e "${CYAN}${BOLD}  ║${RESET}              ${YELLOW}${BOLD}SYSTEM INITIALIZATION${RESET}              ${CYAN}${BOLD}║${RESET}"
echo -e "${CYAN}${BOLD}  ╠════════════════════════════════════════════════════════╣${RESET}"
echo -e "${CYAN}${BOLD}  ║${RESET}          ${WHITE}${BOLD}Preparing your environment...${RESET}          ${CYAN}${BOLD}║${RESET}"
echo -e "${CYAN}${BOLD}  ╚════════════════════════════════════════════════════════╝${RESET}"
echo ""

loading "Initializing ARIYAN System" 25

# ============================================================
#                    PYTHON INSTALL
# ============================================================

header "PYTHON ENVIRONMENT"

if command -v python3 >/dev/null 2>&1; then

    loading "Detecting Python" 18
    echo -e "  ${GREEN}${BOLD}● Python detected${RESET}"
    echo -e "  ${DIM}$(python3 --version)${RESET}"

else

    loading "Installing Python" 25

    pkg install python -y >/dev/null 2>&1

    if ! command -v python3 >/dev/null 2>&1; then
        echo -e "  ${RED}${BOLD}✖ Python installation failed${RESET}"
        exit 1
    fi

    echo -e "  ${GREEN}${BOLD}● Python installed successfully${RESET}"

fi

sleep 0.5

# ============================================================
#                         PIP
# ============================================================

header "PIP ENGINE"

loading "Preparing pip engine" 20

python3 -m pip install --upgrade pip >/dev/null 2>&1

if [ $? -eq 0 ]; then
    echo -e "  ${GREEN}${BOLD}● pip engine ready${RESET}"
else
    echo -e "  ${YELLOW}${BOLD}● pip upgrade skipped${RESET}"
fi

sleep 0.5

# ============================================================
#                       MODULES
# ============================================================

header "MODULE INSTALLATION"

MODULES=(
    "psutil"
    "requests"
    "PyJWT"
    "urllib3"
    "aiohttp"
    "flask"
    "pycryptodome"
    "protobuf"
    "blackboxprotobuf"
    "protobuf-decoder"
    "google-play-scraper"
    "pytz"
    "pyfiglet"
)

TOTAL=${#MODULES[@]}
DONE=0
FAILED=()

for MODULE in "${MODULES[@]}"; do

    DONE=$((DONE + 1))

    echo ""
    echo -e "  ${RGB[$((DONE % RGB_LEN))]}${BOLD}╭──────────────────────────────────────────────────────╮${RESET}"
    echo -e "  ${RGB[$((DONE % RGB_LEN))]}${BOLD}│${RESET}  ${WHITE}${BOLD}${MODULE}${RESET}"
    echo -e "  ${RGB[$((DONE % RGB_LEN))]}${BOLD}╰──────────────────────────────────────────────────────╯${RESET}"

    (
        python3 -m pip install "$MODULE" -q \
            >/tmp/ariyan_install_log 2>&1
        echo $? > /tmp/ariyan_install_status
    ) &

    PID=$!
    FRAME_INDEX=0

    while kill -0 "$PID" 2>/dev/null; do

        COLOR="${RGB[$((FRAME_INDEX % RGB_LEN))]}"

        SPIN=(
            "◐"
            "◓"
            "◑"
            "◒"
        )

        FRAME="${SPIN[$((FRAME_INDEX % 4))]}"

        printf "\r\033[2K"
        echo -ne "  ${COLOR}${BOLD}${FRAME} Installing ${MODULE}...${RESET}"

        FRAME_INDEX=$((FRAME_INDEX + 1))

        sleep 0.08

    done

    wait "$PID" 2>/dev/null

    RESULT=1

    if [ -f /tmp/ariyan_install_status ]; then
        RESULT=$(cat /tmp/ariyan_install_status)
    fi

    rm -f /tmp/ariyan_install_status

    printf "\r\033[2K"

    if [ "$RESULT" -eq 0 ]; then

        echo -e "  ${GREEN}${BOLD}✔ ${MODULE} installed${RESET}"

    else

        echo -e "  ${RED}${BOLD}✖ ${MODULE} failed${RESET}"
        FAILED+=("$MODULE")

    fi

    progress_bar "$DONE" "$TOTAL"

done

rm -f /tmp/ariyan_install_log

# ============================================================
#                    FINAL RGB SHOW
# ============================================================

sleep 1

for round in {1..10}; do

    clear
    echo ""
    echo ""

    i=0

    for line in "${ARIYAN[@]}"; do

        COLOR="${RGB[$(( (i + round) % RGB_LEN ))]}"

        echo -e "  ${COLOR}${BOLD}${line}${RESET}"

        i=$((i + 1))

    done

    echo ""
    echo -e "  ${RGB[$((round % RGB_LEN))]}${BOLD}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${RESET}"
    echo -e "  ${WHITE}${BOLD}                 SYSTEM READY                     ${RESET}"
    echo -e "  ${RGB[$(((round + 5) % RGB_LEN))]}${BOLD}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${RESET}"

    sleep 0.12

done

# ============================================================
#                  FINAL BIG MESSAGE
# ============================================================

clear

echo ""
echo ""

i=0

for line in "${ARIYAN[@]}"; do

    COLOR="${RGB[$((i % RGB_LEN))]}"

    echo -e "  ${COLOR}${BOLD}${line}${RESET}"

    i=$((i + 1))

done

echo ""
echo ""

echo -e "${GREEN}${BOLD}  ╔════════════════════════════════════════════════════════╗${RESET}"
echo -e "${GREEN}${BOLD}  ║                                                        ║${RESET}"
echo -e "${GREEN}${BOLD}  ║              ✦  SETUP COMPLETE  ✦                    ║${RESET}"
echo -e "${GREEN}${BOLD}  ║                                                        ║${RESET}"
echo -e "${GREEN}${BOLD}  ╚════════════════════════════════════════════════════════╝${RESET}"

echo ""

if [ ${#FAILED[@]} -eq 0 ]; then

    echo -e "${CYAN}${BOLD}  ╔════════════════════════════════════════════════════════╗${RESET}"
    echo -e "${CYAN}${BOLD}  ║                                                        ║${RESET}"
    echo -e "${YELLOW}${BOLD}  ║             ★ YOU ARE READY TO SPIN ★                 ║${RESET}"
    echo -e "${CYAN}${BOLD}  ║                                                        ║${RESET}"
    echo -e "${CYAN}${BOLD}  ╚════════════════════════════════════════════════════════╝${RESET}"

else

    echo -e "${YELLOW}${BOLD}  Some modules could not be installed.${RESET}"

    for MODULE in "${FAILED[@]}"; do
        echo -e "  ${RED}${BOLD}✖ ${MODULE}${RESET}"
    done

fi

echo ""
echo -e "${PURPLE}${BOLD}  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${RESET}"
echo -e "${HOT}${BOLD}                       ARIYAN                        ${RESET}"
echo -e "${PURPLE}${BOLD}  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${RESET}"
echo ""

show_cursor

exit 0
