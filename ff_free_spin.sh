#!/data/data/com.termux/files/usr/bin/bash

# ============================================================
#         FREE FIRE SPEN BOT - TERMUX AUTO SETUP
# ============================================================

RESET="\033[0m"
BOLD="\033[1m"
DIM="\033[2m"
GREEN="\033[92m"
YELLOW="\033[93m"
CYAN="\033[96m"
RED="\033[91m"
BLUE="\033[94m"
WHITE="\033[97m"
ORANGE="\033[38;5;214m"
PINK="\033[38;5;206m"
PURPLE="\033[38;5;129m"

# আরিয়ান কালার প্যালেট
RGB=(
    "\033[38;5;196m"  # লাল
    "\033[38;5;208m"  # কমলা
    "\033[38;5;226m"  # হলুদ
    "\033[38;5;118m"  # গ্রিন
    "\033[38;5;51m"   # সায়ান
    "\033[38;5;45m"   # নীল
    "\033[38;5;93m"   # পার্পল
    "\033[38;5;201m"  # ম্যাজেন্টা
    "\033[38;5;198m"  # পিঙ্ক
    "\033[38;5;214m"  # অরেঞ্জ
    "\033[38;5;220m"  # সোনালী
    "\033[38;5;154m"  # চুন
    "\033[38;5;57m"   # ইন্ডিগো
    "\033[38;5;129m"  # ভায়োলেট
    "\033[38;5;212m"  # হট পিঙ্ক
)
RGB_LEN=15

FLASH=("$RED" "$ORANGE" "$YELLOW" "$WHITE" "$PINK" "$PURPLE" "$CYAN" "$GREEN" "$ORANGE" "$RED" "$YELLOW" "$PINK" "$PURPLE")

# ============================================================
# FREE FIRE LOGO (আরিয়ান ভার্সন)
# ============================================================
FF_L0="            ⣀⣠⡤                        "
FF_L1="   ⢀⣤⡶⠁⣠⣴⣾⠟⠋⠁                          "
FF_L2="  ⢀⣴⣿⣿⣴⣿⠿⠋⣁⣀⣀⣀⣀⣀⡀                      "
FF_L3="  ⣰⣿⣿⣿⣿⣿⣷⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣄⡀                "
FF_L4="⣠⣾⣿⡿⠟⠋⠉⠀⣀⣀⣨⣭⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⣤⣤⣤⣴⠂"
FF_L5="⠈⠉⠁⠀⣀⣴⣾⣿⣿⡿⠟⠛⠉⠉⠉⠉⠛⠻⠿⠿⠿⠿⠿⠿⠟⠋⠁          "
FF_L6="   ⢀⣴⣿⣿⣿⡿⠁⢀⣀⣤⣤⣤⣤⣀⣀                      "
FF_L7="   ⣾⣿⣿⣿⡿⠁⢀⣴⣿⠋⠉⠉⠉⠉⠛⣿⣿⣶⣤⣤⣤⣤⣶⠖            "
FF_L8="  ⢸⣿⣿⣿⣿⡇⢀⣿⣿⣇⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⡿⠃              "
FF_L9="  ⠸⣿⣿⣿⣿⡇⠈⢿⣿⣿⠇⠀⠀⠀⠀⢠⣿⣿⣿⠟⠋                "
FF_LA="   ⢿⣿⣿⣿⣷⡀⠀⠉⠉⠀⠀⠀⢀⣾⣿⣿⡏                    "
FF_LB="    ⠙⢿⣿⣿⣷⣄⡀⠀⠀⣀⣴⣿⣿⣿⣋⣠⡤⠄                  "
FF_LC="       ⠈⠙⠛⠛⠿⠿⠿⠿⠿⠟⠛⠛⠛⠉⠁                   "

print_ff_logo() {
    local offset=${1:-0}
    local dim=${2:-0}
    local ri=$(( RANDOM % RGB_LEN ))
    local rc="${RGB[$ri]}"

    echo -e "  ${rc}${BOLD} ⚡ ফ্রি ফায়ার স্পেন বট সেটআপ চলছে... ⚡${RESET}"
    echo ""

    local lines=("$FF_L0" "$FF_L1" "$FF_L2" "$FF_L3" "$FF_L4" "$FF_L5" "$FF_L6" "$FF_L7" "$FF_L8" "$FF_L9" "$FF_LA" "$FF_LB" "$FF_LC")
    local i
    for i in $(seq 0 12); do
        local ci=$(( (i + offset) % 13 ))
        local c="${FLASH[$ci]}"
        if [ "$dim" -eq 1 ] && [ $(( i % 2 )) -ne 0 ]; then
            echo -e "  ${PURPLE}${DIM}${lines[$i]}${RESET}"
        else
            echo -e "  ${c}${BOLD}${lines[$i]}${RESET}"
        fi
    done
    echo ""
}

# ============================================================
# ANIMATION
# ============================================================
ANIM_PID=""
FF_FLAG="${TMPDIR:-$HOME}/_ariyan_ff_flag"
LOGO_ROWS=16
STATUS_ROW=$(( LOGO_ROWS + 2 ))

start_anim() {
    touch "$FF_FLAG"
    (
        local offset=0
        while [ -f "$FF_FLAG" ]; do
            printf "\033[H"
            local mode=$(( offset % 3 ))
            if [ "$mode" -eq 2 ]; then
                print_ff_logo "$offset" 1
            else
                print_ff_logo "$offset" 0
            fi
            offset=$(( (offset + 1) % 39 ))
            sleep 0.12
        done
    ) &
    ANIM_PID=$!
}

stop_anim() {
    rm -f "$FF_FLAG" 2>/dev/null
    [ -n "$ANIM_PID" ] && kill "$ANIM_PID" 2>/dev/null && wait "$ANIM_PID" 2>/dev/null
    ANIM_PID=""
}

# ============================================================
# RGB PROGRESS BAR
# ============================================================
rgb_bar() {
    local filled=$1
    local total=30
    local bar=""
    for i in $(seq 1 $total); do
        local ci=$(( (i + filled) % RGB_LEN ))
        local c="${RGB[$ci]}"
        if [ "$i" -le "$filled" ]; then
            bar="${bar}${c}${BOLD}█${RESET}"
        else
            bar="${bar}${DIM}░${RESET}"
        fi
    done
    echo -ne "$bar"
}

print_status() {
    local idx=$1
    local total=$2
    local name=$3
    local state=$4
    local pct=$(( idx * 100 / total ))
    local filled=$(( idx * 30 / total ))
    local ci=$(( idx % RGB_LEN ))
    local c="${RGB[$ci]}"

    printf "\033[%d;0H\033[2K" "$STATUS_ROW"
    echo -ne "  "
    rgb_bar "$filled"
    echo ""

    printf "\033[%d;0H\033[2K" "$(( STATUS_ROW + 1 ))"
    if   [ "$state" = "ok" ];   then echo -e "  ${GREEN}${BOLD}[✔] $name ${RESET} ${GREEN}✅ সফল${RESET}  ($pct%)"
    elif [ "$state" = "fail" ]; then echo -e "  ${RED}${BOLD}[✗] $name ${RESET} ${RED}❌ ব্যর্থ${RESET}  ($pct%)"
    else                             echo -e "  ${c}${BOLD}⬇️  ইনস্টল হচ্ছে: $name ${RESET}  ($pct%)"
    fi
}

# ============================================================
# ডাউনলোড অ্যানিমেশন
# ============================================================
download_animation() {
    local folder_name="$1"
    local repo_url="https://github.com/Ariyan20267/Gen.git"
    local target_path="$2"
    
    echo -e "${CYAN}${BOLD}  ══════════════════════════════════════════════${RESET}"
    echo -e "${PINK}${BOLD}     📥 ${folder_name} ডাউনলোড হচ্ছে...${RESET}"
    echo -e "${CYAN}${BOLD}  ══════════════════════════════════════════════${RESET}"
    echo ""
    
    # স্পিনার অ্যানিমেশন
    local spin_chars=("⣾" "⣽" "⣻" "⢿" "⡿" "⣟" "⣯" "⣷")
    local colors=("$RED" "$ORANGE" "$YELLOW" "$GREEN" "$CYAN" "$BLUE" "$PURPLE" "$PINK")
    local dots=("⠋" "⠙" "⠹" "⠸" "⠼" "⠴" "⠦" "⠧" "⠇" "⠏")
    
    # ১০ সেকেন্ডের জন্য অ্যানিমেশন চলবে (বাস্তবে ক্লোনিং দ্রুত শেষ হলে থামবে)
    local pid=""
    local temp_dir="${TMPDIR:-/tmp}/download_anim"
    mkdir -p "$temp_dir"
    local flag_file="$temp_dir/running"
    echo "1" > "$flag_file"
    
    # অ্যানিমেশন প্রক্রিয়া
    (
        local i=0
        while [ -f "$flag_file" ]; do
            local c_idx=$(( i % ${#colors[@]} ))
            local sp_idx=$(( i % ${#spin_chars[@]} ))
            local d_idx=$(( (i / 2) % ${#dots[@]} ))
            local color="${colors[$c_idx]}"
            local spinner="${spin_chars[$sp_idx]}"
            local dot="${dots[$d_idx]}"
            
            # এলোমেলো বার্তা
            local msgs=(
                "📦 ফাইল সংগ্রহ করা হচ্ছে"
                "🔍 রিপোজিটরি খোঁজা হচ্ছে"
                "⚡ ডেটা ট্রান্সফার চলছে"
                "📁 ফোল্ডার তৈরি হচ্ছে"
                "🔄 ফাইল সিঙ্ক্রোনাইজ করা হচ্ছে"
                "🚀 ডাউনলোড প্রগতি"
                "💫 ফাইল প্রক্রিয়াকরণ"
                "✨ আপডেট চলছে"
            )
            local msg="${msgs[$(( i % ${#msgs[@]} ))]}"
            
            # প্রগ্রেস বার তৈরি
            local progress=$(( (i * 100) / 60 ))
            [ $progress -gt 95 ] && progress=95
            local bar_len=$(( progress * 40 / 100 ))
            local bar=""
            for j in $(seq 1 40); do
                if [ $j -le $bar_len ]; then
                    local ci=$(( (j + i) % RGB_LEN ))
                    bar="${bar}${RGB[$ci]}█${RESET}"
                else
                    bar="${bar}${DIM}░${RESET}"
                fi
            done
            
            printf "\033[1A\033[2K"  # লাইন মুছে উপরে যাও
            printf "\r  ${color}${BOLD}${spinner} ${dot} ${msg}${RESET}\n"
            printf "  ${color}${BOLD}[${bar}] ${progress}%%${RESET}\n"
            printf "  ${DIM}ফোল্ডার: ${folder_name}${RESET}\n"
            
            i=$((i + 1))
            sleep 0.15
        done
    ) &
    local anim_pid=$!
    
    # আসল ডাউনলোড/ক্লোন কাজ
    if [ -d "$target_path/.git" ]; then
        git -C "$target_path" pull 2>/dev/null
        local result=$?
    else
        rm -rf "$target_path" 2>/dev/null
        git clone --depth 1 "$repo_url" "$target_path" 2>/dev/null
        local result=$?
    fi
    
    # অ্যানিমেশন থামানো
    rm -f "$flag_file"
    wait $anim_pid 2>/dev/null
    
    # ক্লিনআপ
    rm -rf "$temp_dir"
    
    # ফলাফল দেখানো
    if [ $result -eq 0 ] && [ -f "$target_path/main.py" ]; then
        printf "\033[2A\033[2K"  # ২ লাইন উপরে
        printf "\r  ${GREEN}${BOLD}✅ ${folder_name} ডাউনলোড সম্পূর্ণ!${RESET}\n"
        printf "  ${GREEN}${BOLD}🚀 main.py রান করার জন্য প্রস্তুত${RESET}\n"
        sleep 1
        return 0
    else
        printf "\033[2A\033[2K"
        printf "\r  ${RED}${BOLD}❌ ডাউনলোড ব্যর্থ!${RESET}\n"
        printf "  ${YELLOW}${BOLD}⚠️  ইন্টারনেট কানেকশন চেক করুন${RESET}\n"
        sleep 2
        return 1
    fi
}

# ============================================================
# STEP 1 — Storage Permission
# ============================================================
clear
echo -e "${CYAN}${BOLD}  [*] স্টোরেজ অনুমতি চেক করা হচ্ছে...${RESET}"

STORAGE_OK=0

if [ -d ~/storage/shared ] || [ -d ~/storage/downloads ]; then
    STORAGE_OK=1
fi

if [ "$STORAGE_OK" -eq 1 ]; then
    if ! touch ~/storage/downloads/.test_write 2>/dev/null; then
        STORAGE_OK=0
    else
        rm -f ~/storage/downloads/.test_write 2>/dev/null
    fi
fi

if [ "$STORAGE_OK" -eq 0 ]; then
    echo -e "${YELLOW}${BOLD}  [!] স্টোরেজ অনুমতি পাওয়া যায়নি!${RESET}"
    echo -e "${YELLOW}${BOLD}  [!] অনুমতি চাওয়া হচ্ছে...${RESET}"
    termux-setup-storage
    sleep 3
    echo -e "${GREEN}${BOLD}  [✔] অনুমতি দেওয়া হয়েছে!${RESET}"
else
    echo -e "${GREEN}${BOLD}  [✔] স্টোরেজ অনুমতি আগে থেকেই আছে${RESET}"
fi
echo ""

# ============================================================
# STEP 2 — pkg update
# ============================================================
echo -e "${CYAN}${BOLD}  [*] প্যাকেজ আপডেট করা হচ্ছে...${RESET}"
pkg update -y 2>/dev/null || true
pkg upgrade -y 2>/dev/null
echo -e "${GREEN}${BOLD}  [✔] প্যাকেজ আপডেট সম্পূর্ণ${RESET}"
echo ""

# ============================================================
# STEP 3 — Python
# ============================================================
echo -e "${CYAN}${BOLD}  [*] পাইথন চেক করা হচ্ছে...${RESET}"
if command -v python3 &>/dev/null; then
    echo -e "${GREEN}${BOLD}  [✔] পাইথন: $(python3 --version)${RESET}"
else
    echo -e "${YELLOW}${BOLD}  [!] পাইথন ইনস্টল করা হচ্ছে...${RESET}"
    pkg install python -y
    command -v python3 &>/dev/null || { echo -e "${RED}${BOLD}  [✗] পাইথন ইনস্টল ব্যর্থ!${RESET}"; exit 1; }
    echo -e "${GREEN}${BOLD}  [✔] পাইথন ইনস্টল সম্পূর্ণ${RESET}"
fi
echo ""

# ============================================================
# STEP 4 — pip
# ============================================================
echo -e "${CYAN}${BOLD}  [*] পাইপ আপগ্রেড করা হচ্ছে...${RESET}"
python3 -m pip install --upgrade pip -q 2>/dev/null
echo -e "${GREEN}${BOLD}  [✔] পাইপ প্রস্তুত${RESET}"
echo ""

# ============================================================
# STEP 5 — Git
# ============================================================
echo -e "${CYAN}${BOLD}  [*] গিট চেক করা হচ্ছে...${RESET}"
if command -v git &>/dev/null; then
    echo -e "${GREEN}${BOLD}  [✔] গিট: $(git --version)${RESET}"
else
    pkg install git -y
    command -v git &>/dev/null || { echo -e "${RED}${BOLD}  [✗] গিট ইনস্টল ব্যর্থ!${RESET}"; exit 1; }
    echo -e "${GREEN}${BOLD}  [✔] গিট ইনস্টল সম্পূর্ণ${RESET}"
fi
echo ""

# ============================================================
# STEP 6-7 — MODULE INSTALL (সুন্দর ডিজাইন)
# ============================================================

BOX_W=50
B="${PINK}${BOLD}"
RS="${RESET}"

box_top()  { echo -e "${B}  ╔$(printf '═%.0s' $(seq 1 $BOX_W))╗${RS}"; }
box_bot()  { echo -e "${B}  ╚$(printf '═%.0s' $(seq 1 $BOX_W))╝${RS}"; }
box_line() { echo -e "${B}  ╠$(printf '═%.0s' $(seq 1 $BOX_W))╣${RS}"; }
box_empty(){ printf "${B}  ║${RS}%-${BOX_W}s${B}║${RS}\n" ""; }

box_center() {
    local text="$1" color="${2:-$WHITE}"
    local clean; clean=$(echo -e "$text" | sed 's/\x1b\[[0-9;]*m//g')
    local tlen=${#clean}
    local lpad=$(( (BOX_W - tlen) / 2 ))
    local rpad=$(( BOX_W - tlen - lpad ))
    printf "${B}  ║${RS}%${lpad}s${color}${BOLD}%s${RS}%${rpad}s${B}║${RS}\n" "" "$text" ""
}

box_left() {
    local text="$1" color="${2:-$WHITE}"
    local clean; clean=$(echo -e "$text" | sed 's/\x1b\[[0-9;]*m//g')
    local pad=$(( BOX_W - ${#clean} - 2 ))
    [ $pad -lt 0 ] && pad=0
    printf "${B}  ║${RS} ${color}${BOLD}%s${RS}%${pad}s${B} ║${RS}\n" "$text" ""
}

# ── আরিয়ান লোগো লাইন ──
LOGO_LINES=(
    "░█████╗░██████╗░██╗██╗   ██╗░█████╗░███╗░░██╗"
    "██╔══██╗██╔══██╗██║╚██╗ ██╔╝██╔══██╗████╗░██║"
    "███████║██████╔╝██║ ╚████╔╝ ███████║██╔██╗██║"
    "██╔══██║██╔══██╗██║  ╚██╔╝  ██╔══██║██║╚████║"
    "██║  ██║██║  ██║██║   ██║   ██║  ██║██║ ╚███║"
    "╚═╝  ╚═╝╚═╝  ╚═╝╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚══╝"
)

flash_logo() {
    local colors=("$RED" "$ORANGE" "$YELLOW" "$GREEN" "$CYAN" "$BLUE" "$PURPLE" "$PINK" "$WHITE")
    local ci=0
    for round in 1 2 3 4; do
        printf "\033[8A"
        box_line
        for line in "${LOGO_LINES[@]}"; do
            local c="${colors[$ci]}"
            ci=$(( (ci + 1) % ${#colors[@]} ))
            box_center "$line" "$c"
        done
        box_line
        sleep 0.15
    done
}

rgb_progress_box() {
    local done=$1 total=$2
    local filled=$(( done * (BOX_W - 4) / total ))
    local empty=$(( BOX_W - 4 - filled ))
    local bar=""
    local ci=0
    for i in $(seq 1 $filled); do
        ci=$(( (i + done) % RGB_LEN ))
        bar="${bar}${RGB[$ci]}${BOLD}▰${RESET}"
    done
    for i in $(seq 1 $empty); do
        bar="${bar}${DIM}▱${RESET}"
    done
    printf "${B}  ║${RS} ${bar} ${B}║${RS}\n"
}

# ══════════════════ বক্স আঁকা শুরু ══════════════════
clear
box_top
box_center "⚡ 𝗙𝗥𝗘𝗘 𝗙𝗜𝗥𝗘 𝗦𝗣𝗘𝗡 𝗕𝗢𝗧 ⚡" "$YELLOW"
box_center "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" "$YELLOW"
box_line

for line in "${LOGO_LINES[@]}"; do
    box_center "$line" "$CYAN"
done
box_line

flash_logo

box_center "📦  মডিউল ইনস্টল করা হচ্ছে  📦" "$YELLOW"
box_line

FAILED=()
MODULES=(
    "requests|pip"
    "pycryptodome|pip"
    "psutil|pip"
    "protobuf|pip"
    "blackboxprotobuf|pip"
)
TOTAL=${#MODULES[@]}
DONE=0

for entry in "${MODULES[@]}"; do
    name="${entry%%|*}"
    method="${entry##*|}"
    DONE=$(( DONE + 1 ))

    box_left "  ⏳ ${name}  [${DONE}/${TOTAL}]" "$YELLOW"

    if [ "$method" = "pkg" ]; then
        pkg install "python-${name}" -y &>/dev/null || python3 -m pip install "$name" -q &>/dev/null
    else
        python3 -m pip install "$name" -q &>/dev/null
    fi

    if [ $? -eq 0 ]; then
        printf "\033[1A\033[2K"
        box_left "  ✅ ${name} (সফল)" "$GREEN"
    else
        printf "\033[1A\033[2K"
        box_left "  ❌ ${name} (ব্যর্থ)" "$RED"
        FAILED+=("$name")
    fi

    rgb_progress_box "$DONE" "$TOTAL"
    printf "\033[1A"
done

echo ""
rgb_progress_box "$TOTAL" "$TOTAL"
box_bot

# ============================================================
# FINAL REPORT
# ============================================================
clear
print_ff_logo 4 0
echo -e "${BLUE}${BOLD}  ══════════════════════════════════════════════${RESET}"
if [ ${#FAILED[@]} -gt 0 ]; then
    echo -e "${YELLOW}${BOLD}  [!] ব্যর্থ মডিউল:${RESET}"
    for f in "${FAILED[@]}"; do
        echo -e "  ${RED}    ❌ $f${RESET}"
    done
    echo -e "${YELLOW}${BOLD}  [!] ইন্টারনেট চেক করে আবার চেষ্টা করুন।${RESET}"
else
    echo -e "${GREEN}${BOLD}  [✔] সব মডিউল সফলভাবে ইনস্টল হয়েছে! 😊${RESET}"
fi
echo -e "${BLUE}${BOLD}  ══════════════════════════════════════════════${RESET}"
echo ""

# ============================================================
# WHATSAPP GROUP JOIN
# ============================================================

WHATSAPP_LINK="https://whatsapp.com/channel/0029Vb7jk7n6mYPIZIHDeV1T"

echo -e "${CYAN}${BOLD}  [*] WhatsApp গ্রুপে জয়েন করা হচ্ছে...${RESET}"
sleep 1

if command -v termux-open &>/dev/null; then
    termux-open "$WHATSAPP_LINK"
else
    am start -a android.intent.action.VIEW -d "$WHATSAPP_LINK" 2>/dev/null || true
fi

echo -e "${GREEN}${BOLD}  [✔] WhatsApp ওপেন করা হয়েছে${RESET}"
sleep 2

# ============================================================
# FREE FIRE SPEN ডাউনলোড (সুন্দর অ্যানিমেশন সহ)
# ============================================================

clear
echo -e "${PURPLE}${BOLD}  ══════════════════════════════════════════════${RESET}"
echo -e "${PURPLE}${BOLD}     🎮 FREE FIRE SPEN - ডাউনলোড ও সেটআপ 🎮${RESET}"
echo -e "${PURPLE}${BOLD}  ══════════════════════════════════════════════${RESET}"
echo ""

# ফোল্ডার পাথ নির্ধারণ
STORAGE_PATH="/sdcard/free fire spen"
[ ! -d "/sdcard" ] && [ -d "/storage/emulated/0" ] && STORAGE_PATH="/storage/emulated/0/free fire spen"

# ডাউনলোড অ্যানিমেশন চালানো
if download_animation "free fire spen" "$STORAGE_PATH"; then
    echo ""
    echo -e "${GREEN}${BOLD}  ✅ ফাইল প্রস্তুত!${RESET}"
    echo -e "${CYAN}${BOLD}  🚀 main.py রান করা হচ্ছে...${RESET}"
    echo ""
    sleep 2
    clear
    
    # আরিয়ান লোগো দেখানো
    print_ff_logo 0 0
    
    echo -e "${GREEN}${BOLD}  ══════════════════════════════════════════════${RESET}"
    echo -e "${GREEN}${BOLD}     🚀 FREE FIRE SPEN BOT চালু হচ্ছে... 🚀${RESET}"
    echo -e "${GREEN}${BOLD}  ══════════════════════════════════════════════${RESET}"
    echo ""
    sleep 1
    
    cd "$STORAGE_PATH" && python3 main.py
else
    echo ""
    echo -e "${RED}${BOLD}  ❌ ডাউনলোড ব্যর্থ!${RESET}"
    echo -e "${YELLOW}${BOLD}  ⚠️  অনুগ্রহ করে ইন্টারনেট কানেকশন চেক করুন${RESET}"
    echo -e "${YELLOW}${BOLD}  ⚠️  এবং আবার চেষ্টা করুন${RESET}"
    echo ""
    exit 1
fi
