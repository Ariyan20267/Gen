#!/usr/bin/env python3
# ╔════════════════════════════════════════════════════════════════════════════╗
# ║                                                                            ║
# ║         ██████╗  ██████╗  ██╗██╗   ██╗ █████╗ ███╗   ██╗                 ║
# ║         ██╔══██╗ ██╔═══██╗ ██║╚██╗ ██╔╝██╔══██╗████╗  ██║                 ║
# ║         ██████╔╝ ██║   ██║ ██║ ╚████╔╝ ███████║██╔██╗ ██║                 ║
# ║         ██╔══██╗ ██║   ██║ ██║  ╚██╔╝  ██╔══██║██║╚██╗██║                 ║
# ║         ██║  ██║ ██║  ██║╚██╔██╔╝███████║██║  ██║██║  ██║                 ║
# ║         ╚═╝  ╚═╝  ╚═════╝  ╚══╝╚══╝ ╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝                 ║
# ║                                                                            ║
# ║                    ARIYAN ULTIMATE GENERATOR v12.1                         ║
# ║              THE MOST ADVANCED ACCOUNT GENERATOR                         ║
# ║                    WITH ULTIMATE ADMIN CONTROL                            ║
# ║                                                                            ║
# ║         CREDIT: ARIYAN  |  GITHUB: github.com/Ariyan                     ║
# ║              TELEGRAM: @Ariyan  |  @Ariyan                                ║
# ║                                                                            ║
# ║         WATERMARKS: ULTIMATE_PROTECTION_v12_OB54                        ║
# ║            PROTECTED_BY_ARIYAN ADMIN_CONTROL_SYSTEM                      ║
# ║                    OWNER_VERIFICATION OWNER MODE                          ║
# ╚════════════════════════════════════════════════════════════════════════════╝
# =============================================================================

# ╔══════════════════════════════════════════════════╗
# ║              LICENSE EXPIRY LOCK                 ║
# ║     Paste this block at the TOP of your file     ║
# ║         Only change the EXPIRY_DATE below        ║
# ╚══════════════════════════════════════════════════╝

import datetime as __dt
import os as __os
import sys as __sys
import time as __tm

__EXPIRY_DATE = "2027-07-15"  # <-- Set your expiry date here (YYYY-MM-DD)

__today = __dt.date.today()
__limit = __dt.date.fromisoformat(__EXPIRY_DATE)

if __today > __limit:
    __gone = (__today - __limit).days
    __R  = "\033[0m"
    __RE = "\033[1;31m"
    __Y  = "\033[1;33m"
    __DM = "\033[2;37m"
    __C  = "\033[1;36m"
    print(f"{__RE}")
    print(f"  ╔══════════════════════════════════════════════╗")
    print(f"  ║         ⛔  LICENSE EXPIRED                  ║")
    print(f"  ╠══════════════════════════════════════════════╣")
    print(f"  ║  {__Y}Expiry Date  : {__EXPIRY_DATE}{__RE}                    ║")
    print(f"  ║  {__Y}Today        : {__today}{__RE}                    ║")
    print(f"  ║  {__Y}Expired      : {__gone} day(s) ago{__RE}                ║")
    print(f"  ╠══════════════════════════════════════════════╣")
    print(f"  ║  {__C}main.py will now be permanently deleted.{__RE}  ║")
    print(f"  ╚══════════════════════════════════════════════╝{__R}")
    __tm.sleep(2)
    
    # Delete main.py from the same folder
    try:
        __script_dir = __os.path.dirname(__os.path.abspath(__sys.argv[0]))
        __main_file = __os.path.join(__script_dir, "main.py")
        
        if __os.path.exists(__main_file):
            __os.remove(__main_file)
            print(f"{__DM}  ✓ main.py deleted successfully.{__R}")
        else:
            print(f"{__Y}  ⚠ main.py not found in this folder.{__R}")
    except Exception as __err:
        print(f"{__RE}  ✗ Could not delete main.py: {__err}{__R}")
    
    __sys.exit(1)

del __dt, __os, __sys, __tm
del __today, __limit, __EXPIRY_DATE

# ══════════════════════════════════════════════════
#          Your actual code starts below
# ══════════════════════════════════════════════════
import hmac
import hashlib
import requests
import string
import random
import json
import codecs
import time
from datetime import datetime
import os
import sys
import base64
import signal
import threading
import psutil
import re
import subprocess
import importlib
import logging
import warnings
import urllib3
import shutil
import inspect
import platform
import getpass
import asyncio

# Disable warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
warnings.filterwarnings("ignore")

# Include PB2 path inside project dynamically
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'Pb2'))

# =============================================================================
# 🛡️ ULTIMATE ANTI-CREDIT & FILENAME PROTECTION SYSTEM
# =============================================================================

class SecurityShield:
    """Security checks removed"""
    @classmethod
    def verify_filename(cls): return True
    @classmethod
    def verify_credits(cls): return True, "OK"
    @classmethod
    def show_breach(cls, reason): pass

# =============================================================================
# 🎨 ULTIMATE VISUAL MASTER - RGB NEON CYAN & MAGENTA THEME
# =============================================================================

class VisualMaster:
    """Professional visual design system - RGB Neon Cyan & Electric Magenta Theme"""

    COLORS = {
        # ── RGB cyber-neon palette ──────────────────────────────────────────
        'primary':   '\033[38;5;201m',    # Neon hot pink / magenta
        'secondary': '\033[38;5;51m',     # Electric neon cyan
        'success':   '\033[38;5;82m',     # Neon lime green
        'error':     '\033[38;5;196m',    # Electric red
        'warning':   '\033[38;5;226m',    # Bright yellow
        'rare':      '\033[38;5;208m',    # Intense neon orange
        'couple':    '\033[38;5;135m',    # Vivid violet/purple
        'info':      '\033[38;5;33m',     # Cyber blue
        'highlight': '\033[38;5;226m',    # Bright yellow
        'dim':       '\033[38;5;241m',    # Deep metallic grey
        'owner':     '\033[38;5;201m',
        'admin':     '\033[38;5;51m',
        'user':      '\033[38;5;82m',
        'border':    '\033[38;5;51m',     # Neon cyan borders
        'accent':    '\033[38;5;255m',    # Bright white
        'reset':     '\033[0m',
        'bold':      '\033[1m',
        'italic':    '\033[3m',
        'bg_dark':   '\033[48;5;16m',
        # ── vivid box-content colors ───────────────────────────────────────
        'box_red':   '\033[38;5;196m',   
        'box_yellow':'\033[38;5;226m',   
        'box_green': '\033[38;5;82m',    
        'box_blue':  '\033[38;5;51m',    
        'box_white': '\033[38;5;255m',   
        'box_purple':'\033[38;5;135m',   
        'c1':        '\033[38;5;201m',    # Pink-cyan gradient phase colors
        'c2':        '\033[38;5;165m',
        'c3':        '\033[38;5;129m',
        'c4':        '\033[38;5;51m',
        'c5':        '\033[38;5;82m',
        'c6':        '\033[38;5;226m',
    }

    ICONS = {
        'success': '⚡', 'error': '❌', 'warning': '⚠️',  'info': '💡',
        'rare': '💎',    'couple': '💞', 'fire': '🔥',    'rocket': '🚀',
        'lock': '🔒',    'key': '🔑',   'shield': '🛡️',  'user': '👤',
        'id': '🆔',      'pass': '🔐',  'time': '⏱️',    'speed': '⚡',
        'target': '🎯',  'folder': '📁','stats': '📊',   'globe': '🌍',
        'thread': '🧵',  'crown': '👑', 'star': '⭐',    'heart': '❤️',
        'admin': '👑',   'owner': '💎', 'user_icon': '👤','edit': '✏️',
        'save': '💾',    'config': '⚙️','custom': '🎨',  'credit': '📝',
        'sword': '⚔️',  'diamond': '💠',
    }

    BOX = {
        'tl': '╔', 'tr': '╗', 'bl': '╚', 'br': '╝', 'h': '═', 'v': '║',
        'ml': '╠', 'mr': '╣',
    }

    REGION_FULL_NAMES = {
        "ME": "Middle East", 
        "IND": "India", 
        "ID": "Indonesia", 
        "VN": "Vietnam", 
        "TH": "Thailand",
        "BD": "Bangladesh", 
        "PK": "Pakistan", 
        "TW": "Taiwan", 
        "CIS": "CIS Region", 
        "SAC": "South America", 
        "BR": "Brazil"
    }

    @classmethod
    def center_text(cls, text, width=None):
        if width is None:
            width = shutil.get_terminal_size().columns
        return text.center(width)

    @classmethod
    def create_box(cls, title=None, width=70, height=1):
        lines = []
        C = cls.COLORS
        if title:
            top = f"{C['border']}{cls.BOX['tl']}{cls.BOX['h'] * 2} {C['primary']}{C['bold']}{title}{C['reset']}{C['border']} {cls.BOX['h'] * 2}{cls.BOX['tr']}{C['reset']}"
        else:
            top = f"{C['border']}{cls.BOX['tl']}{cls.BOX['h'] * (width-2)}{cls.BOX['tr']}{C['reset']}"
        lines.append(top)
        for _ in range(height - 1):
            lines.append(f"{C['border']}{cls.BOX['v']}{' ' * (width-2)}{cls.BOX['v']}{C['reset']}")
        bottom = f"{C['border']}{cls.BOX['bl']}{cls.BOX['h'] * (width-2)}{cls.BOX['br']}{C['reset']}"
        lines.append(bottom)
        return lines

    @classmethod
    def create_panel(cls, title, content, width=None, color='primary'):
        if width is None:
            width = shutil.get_terminal_size().columns - 4
        C = cls.COLORS
        lines_content = content.split('\n')
        result = []
        result.append(f"{C['border']}{cls.BOX['tl']}{cls.BOX['h'] * 2} {C[color]}{C['bold']}{title}{C['reset']}{C['border']} {cls.BOX['h'] * max(0, width - len(title) - 6)}{cls.BOX['tr']}{C['reset']}")
        result.append(f"{C['border']}{cls.BOX['v']}{C['reset']}{' ' * (width - 2)}{C['border']}{cls.BOX['v']}{C['reset']}")
        for line in lines_content:
            visible_line = re.sub(r'\033\[[0-9;]*m', '', line)
            pad = max(0, width - len(visible_line) - 4)
            result.append(f"{C['border']}{cls.BOX['v']}{C['reset']}  {C['accent']}{line}{C['reset']}{' ' * pad}  {C['border']}{cls.BOX['v']}{C['reset']}")
        result.append(f"{C['border']}{cls.BOX['v']}{C['reset']}{' ' * (width - 2)}{C['border']}{cls.BOX['v']}{C['reset']}")
        result.append(f"{C['border']}{cls.BOX['bl']}{cls.BOX['h'] * (width - 2)}{cls.BOX['br']}{C['reset']}")
        return '\n'.join(result)

    @classmethod
    def get_input(cls, box_title, instruction_msg, accent_color='primary'):
        """Displays a beautiful, dedicated input box for capturing variables cleanly with colored content"""
        C = cls.COLORS
        W = 60
        border_col = C[accent_color]
        
        # ── First Box ─────────────────────────────────────────────────────────
        lines = []
        lines.append(f"{border_col}╔═ {C['accent']}{C['bold']}{box_title.upper()}{C['reset']}{border_col} {'═' * (W - len(box_title) - 5)}╗{C['reset']}")
        lines.append(f"{border_col}║{C['reset']}  {C['secondary']}{C['bold']}{instruction_msg:<{W-4}}{border_col}║{C['reset']}")
        lines.append(f"{border_col}╚{'═' * (W - 2)}╝{C['reset']}")
        
        for line in lines:
            print(line)
        
        # ── Input ─────────────────────────────────────────────────────────────
        val = input(f"\n  {C['c4']}➤ {C['success']}{C['bold']}ENTER{C['reset']} {C['c6']}» {C['reset']}").strip()
        print()
        return val

    @classmethod
    def create_progress_bar(cls, current, total, width=50):
        C = cls.COLORS
        percent = current / total if total > 0 else 0
        filled = int(width * percent)
        bar = f"{C['primary']}{'█' * filled}{C['dim']}{'░' * (width - filled)}{C['reset']}"
        return f"{bar} {C['bold']}{C['warning']}{percent*100:5.1f}%{C['reset']}"

    @classmethod
    def clear(cls):
        os.system('cls' if os.name == 'nt' else 'clear')

    _header_shown = False

    @classmethod
    def show_header(cls, user_level="USER"):
        if not cls._header_shown:
            cls.clear()
            cls.animate_header(user_level)
            cls._header_shown = True

    @classmethod
    def animate_header(cls, user_level="USER"):
        """Clean and premium cyber launch sequence featuring ARIYAN neon style"""
        import sys, time, shutil as _sh
        W   = _sh.get_terminal_size().columns
        C   = cls.COLORS
        R   = C['reset'];  B = C['bold']

        SH = [C['c1'],C['c2'],C['c3'],C['c4'],C['c5'],C['c6'],
              C['c5'],C['c4'],C['c3'],C['c2'],C['c1']]

        # ══ PHASE 1: Neon expanding border ═══════════════════════════════
        for i in range(0, W-2, 10):
            bar = "═" * min(i, W-2)
            sys.stdout.write(f"\r{C['c1']}{B}╠{bar}▶{R}")
            sys.stdout.flush()
            time.sleep(0.01)
        sys.stdout.write(f"\r{C['c1']}{B}╠{'═'*(W-2)}╣{R}\n")
        sys.stdout.flush()

        # ══ PHASE 2: ARIYAN 3D Art ═════════════════════════════════
        ARIYAN_LOGO = [
            "  ░█████╗░██████╗░██╗██╗░░░██╗░█████╗░███╗░░██╗  ",
            "  ██╔══██╗██╔══██╗██║╚██╗░██╔╝██╔══██╗████╗░██║  ",
            "  ███████║██████╔╝██║░╚████╔╝░███████║██╔██╗██║  ",
            "  ██╔══██║██╔══██╗██║░░╚██╔╝░░██╔══██║██║╚████║  ",
            "  ██║░░██║██║░░██║██║░░░██║░░░██║░░██║██║░╚███║  ",
            "  ╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚══╝  ",
            "",
            "  ███████╗██████╗░███████╗███████╗  ███████╗██╗██████╗░███████╗  ",
            "  ██╔════╝██╔══██╗██╔════╝██╔════╝  ██╔════╝██║██╔══██╗██╔════╝  ",
            "  █████╗░░██████╔╝█████╗░░█████╗░░  █████╗░░██║██████╔╝█████╗░░  ",
            "  ██╔══╝░░██╔══██╗██╔══╝░░██╔══╝░░  ██╔══╝░░██║██╔══██╗██╔══╝░░  ",
            "  ██║░░░░░██║░░██║███████╗███████╗  ██║░░░░░██║██║░░██║███████╗  ",
            "  ╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚══════╝  ╚═╝░░░░░╚═╝╚═╝░░╚═╝╚══════╝  ",
            "",
            "  ░░░░░░░░░  𝗚𝗨𝗘𝗦𝗧  𝗔𝗖𝗖𝗢𝗨𝗡𝗧  𝗚𝗘𝗡𝗘𝗥𝗔𝗧𝗢𝗥  ░░░░░░░░░  ",
        ]
        for i, line in enumerate(ARIYAN_LOGO):
            shade = SH[(i+2) % len(SH)]
            for end in range(1, len(line)+1, 4):
                sys.stdout.write(f"\r{shade}{B}{line[:end].center(W)}{R}")
                sys.stdout.flush()
                time.sleep(0.003)
            sys.stdout.write(f"\r{shade}{B}{line.center(W)}{R}\n")
            sys.stdout.flush()

    @classmethod
    def animate_hand_scan(cls):
        """Dynamic typing & writing hand-animation during ID generation"""
        C = cls.COLORS
        B = C['bold']
        colors = [C['c1'], C['c2'], C['c3'], C['c4'], C['c5'], C['c6']]
        frames = [
            "   ✍️   [ ARIYAN Matrix: Initializing virtual handshake... ]",
            "   👉   [ Injecting custom cryptographic sequence... ]",
            "   ⚡   [ Hooking into dynamic token bypass pools... ]",
            "   🔒   [ Securing dynamic JWT auth variables... ]",
            "   🎮   [ Activating database registration packets... ]",
            "   ✅   [ Success! Extracting account identifiers... ]"
        ]
        for i, frame in enumerate(frames):
            col = colors[i % len(colors)]
            sys.stdout.write(f"\r{col}{B}{frame}{C['reset']}")
            sys.stdout.flush()
            time.sleep(0.12)
        sys.stdout.write("\r" + " " * shutil.get_terminal_size().columns + "\r")
        sys.stdout.flush()


# Initialize Visual Master
VISUAL = VisualMaster()

USER_LEVEL = "OWNER"

# =============================================================================
# ⚡ FAST REQUIREMENTS INSTALLER (RGB ENCLOSED MODULE BOX)
# =============================================================================

def install_requirements():
    required = ['requests', 'pycryptodome', 'colorama', 'psutil', 'protobuf']
    C = VISUAL.COLORS
    
    print(f"{C['c4']}╔══════════════════════════════════════════════════════════╗")
    print(f"{C['c4']}║{C['accent']}{C['bold']}{'SYSTEM DEPENDENCY SYNC UNIT':^56}{C['c4']}║")
    print(f"{C['c4']}╠══════════════════════════════════════════════════════════╣")
    
    for pkg in required:
        status = "SCANNING..."
        print(f"{C['c4']}║ {C['secondary']}{pkg:<25} {C['dim']}... {C['warning']}{status:<15} {C['c4']}║", end="\r")
        try:
            if pkg == 'pycryptodome':
                import Crypto
            elif pkg == 'requests':
                import requests
            elif pkg == 'colorama':
                from colorama import Fore, Style, init
            elif pkg == 'psutil':
                import psutil
            elif pkg == 'protobuf':
                import google.protobuf
            print(f"{C['c4']}║ {C['secondary']}{pkg:<25} {C['dim']}... {C['success']}READY           {C['c4']}║")
        except ImportError:
            print(f"{C['c4']}║ {C['secondary']}{pkg:<25} {C['dim']}... {C['primary']}DOWNLOADING     {C['c4']}║")
            try:
                process = subprocess.Popen(
                    [sys.executable, '-m', 'pip', 'install', '--no-cache-dir', pkg, '-q'],
                    stdout=subprocess.PIPE, stderr=subprocess.PIPE
                )
                stdout, stderr = process.communicate(timeout=30)
                if process.returncode == 0:
                    print(f"{C['c4']}║ {C['secondary']}{pkg:<25} {C['dim']}... {C['success']}INSTALLED       {C['c4']}║")
                else:
                    print(f"{C['c4']}║ {C['secondary']}{pkg:<25} {C['dim']}... {C['error']}FAILED          {C['c4']}║")
            except:
                print(f"{C['c4']}║ {C['secondary']}{pkg:<25} {C['dim']}... {C['error']}ERROR           {C['c4']}║")
    
    print(f"{C['c4']}╚══════════════════════════════════════════════════════════╝")
    print()
    try:
        from colorama import Fore, Style, init
        init(autoreset=True)
    except:
        pass
    time.sleep(1)

install_requirements()

# Import crypto
try:
    from Crypto.Cipher import AES
    from Crypto.Util.Padding import pad, unpad
    AES_AVAILABLE = True
except:
    AES_AVAILABLE = False
    def aes_encrypt(data): return data.encode() if isinstance(data, str) else data

# Import updated protobuf modules from genapi zip
try:
    import MajoRLoGinrEq_pb2
    import MajoRLoGinrEs_pb2
    import PorTs_pb2
    import reqClan_pb2
    NEW_PROTO_AVAILABLE = True
except ImportError:
    NEW_PROTO_AVAILABLE = False

# =============================================================================
# ⚙️ CONFIGURATION - MAX THREADS SUPPORT UP TO 150
# =============================================================================

class Config:
    VERSION = "12.1 ULTIMATE ADMIN CONTROL"
    
    CPU_CORES = psutil.cpu_count()
    MAX_THREADS = min(CPU_CORES * 4, 150)  # ১৫০ পর্যন্ত সাপোর্ট
    
    USER_LEVEL = USER_LEVEL

    SUCCESS = 0; RARE = 0; COUPLES = 0; ACTIVATED = 0; FAILED = 0; BIO = 0; ATTEMPTS = 0
    LOCK = threading.Lock()
    FILE_LOCKS = {}

    EXIT = False
    AUTO_ACT = True
    AUTO_BIO = True
    AUTO_EMOTE = False  # Added Auto Emote Config
    MAX_RETRIES = 5 if USER_LEVEL == "USER" else 10

    # ---- user-defined password prefix ----
    CUSTOM_PASS_PREFIX = "Ariyan"
    CUSTOM_NAME_PREFIX = "Ariyan"
    CUSTOM_RARITY_THRESHOLD = 3
    CUSTOM_TARGET = 999999999
    CURRENT_JSON_BASE = "accounts"
    CURRENT_ACTIVATED_BASE = "accounts-activated"

    # ---- bio generation config variables ----
    BIO_MODE = "Y"
    MX_NAME = "ARIYAN"

    # ---- friend request config variables ----
    SEND_FRIEND_REQ = False
    TARGET_UID = 0
    FRIEND_REQ_SUCCESS_COUNT = 0
    FRIEND_REQ_FAILED_COUNT = 0

    # ---- clan/guild request config variables ----
    SEND_CLAN_REQ = False
    TARGET_CLAN_ID = 0
    CLAN_REQ_SUCCESS_COUNT = 0
    CLAN_REQ_FAILED_COUNT = 0

    if USER_LEVEL in ["ADMIN", "OWNER"]:
        DEBUG_MODE = True
        VERBOSE_LOGGING = True
        MAX_THREADS = min(CPU_CORES * 8, 150)  # ADMIN/OWNER এর জন্য ১৫০ পর্যন্ত
        CAN_EDIT_CREDITS = True
    else:
        DEBUG_MODE = False
        VERBOSE_LOGGING = False
        CAN_EDIT_CREDITS = False

    if USER_LEVEL == "OWNER":
        BYPASS_RATE_LIMIT = True
        FORCE_GENERATION = True
        CUSTOM_API_PRIORITY = True
    else:
        BYPASS_RATE_LIMIT = False
        FORCE_GENERATION = False
        CUSTOM_API_PRIORITY = False

    RARITY_THRESHOLD = 3

    BIO_TEXT = "[FF0000]🌈[FF7700]A[FFFF00]R[00FF00]I[00BFFF]Y[8B00FF]A[FF0000]N[FFFF00]_[00FF00]C[00BFFF]O[8B00FF]D[FF0000]E [FF7700]C[FFFF00]R[00FF00]E[00BFFF]A[8B00FF]T[FF0000]I[FF7700]O[FFFF00]N[FF0000]🌈"

    REGION_LANG = {
        "ME": "ar", "IND": "hi", "ID": "id", "VN": "vi", "TH": "th",
        "BD": "bn", "PK": "ur", "TW": "zh", "CIS": "ru", "SAC": "es", "BR": "pt"
    }

    # ── ACTIVATION_REGIONS: URLs (fastest, zero-fail) ─────────
    ACTIVATION_REGIONS = {
        'IND': {'guest_url': 'https://ffmconnect.live.gop.garenanow.com/oauth/guest/token/grant',
                'major_login_url': 'https://loginbp.common.ggbluefox.com/MajorLogin',
                'get_login_data_url': 'https://client.ind.freefiremobile.com/GetLoginData',
                'client_host': 'client.ind.freefiremobile.com'},
        'BD':  {'guest_url': 'https://ffmconnect.live.gop.garenanow.com/oauth/guest/token/grant',
                'major_login_url': 'https://loginbp.ggpolarbear.com/MajorLogin',
                'get_login_data_url': 'https://clientbp.ggpolarbear.com/GetLoginData',
                'client_host': 'clientbp.ggpolarbear.com'},
        'PK':  {'guest_url': 'https://ffmconnect.live.gop.garenanow.com/oauth/guest/token/grant',
                'major_login_url': 'https://loginbp.ggpolarbear.com/MajorLogin',
                'get_login_data_url': 'https://clientbp.ggpolarbear.com/GetLoginData',
                'client_host': 'clientbp.ggpolarbear.com'},
        'ID':  {'guest_url': 'https://ffmconnect.live.gop.garenanow.com/oauth/guest/token/grant',
                'major_login_url': 'https://loginbp.ggpolarbear.com/MajorLogin',
                'get_login_data_url': 'https://clientbp.ggpolarbear.com/GetLoginData',
                'client_host': 'clientbp.ggpolarbear.com'},
        'TH':  {'guest_url': 'https://ffmconnect.live.gop.garenanow.com/oauth/guest/token/grant',
                'major_login_url': 'https://loginbp.common.ggbluefox.com/MajorLogin',
                'get_login_data_url': 'https://clientbp.common.ggbluefox.com/GetLoginData',
                'client_host': 'clientbp.common.ggbluefox.com'},
        'VN':  {'guest_url': 'https://ffmconnect.live.gop.garenanow.com/oauth/guest/token/grant',
                'major_login_url': 'https://loginbp.ggpolarbear.com/MajorLogin',
                'get_login_data_url': 'https://clientbp.ggpolarbear.com/GetLoginData',
                'client_host': 'clientbp.ggpolarbear.com'},
        'ME':  {'guest_url': 'https://ffmconnect.live.gop.garenanow.com/oauth/guest/token/grant',
                'major_login_url': 'https://loginbp.common.ggbluefox.com/MajorLogin',
                'get_login_data_url': 'https://clientbp.common.ggbluefox.com/GetLoginData',
                'client_host': 'clientbp.common.ggbluefox.com'},
        'BR':  {'guest_url': 'https://ffmconnect.live.gop.garenanow.com/oauth/guest/token/grant',
                'major_login_url': 'https://loginbp.ggpolarbear.com/MajorLogin',
                'get_login_data_url': 'https://clientbp.ggpolarbear.com/GetLoginData',
                'client_host': 'clientbp.ggpolarbear.com'},
        'NA':  {'guest_url': 'https://ffmconnect.live.gop.garenanow.com/oauth/guest/token/grant',
                'major_login_url': 'https://loginbp.ggpolarbear.com/MajorLogin',
                'get_login_data_url': 'https://clientbp.ggpolarbear.com/GetLoginData',
                'client_host': 'clientbp.ggpolarbear.com'},
        'LK':  {'guest_url': 'https://ffmconnect.live.gop.garenanow.com/oauth/guest/token/grant',
                'major_login_url': 'https://loginbp.ggpolarbear.com/MajorLogin',
                'get_login_data_url': 'https://clientbp.ggpolarbear.com/GetLoginData',
                'client_host': 'clientbp.ggpolarbear.com'},
    }

    # ── OB54 FIXED API CONFIGURATION ──────────────────────────────────────────
    HEX_KEY = "2ee44819e9b4598845141067b281621874d0d5d7af9d8f7e00c1e54715b7d1e3"
    API_KEY  = bytes.fromhex(HEX_KEY)

    REGISTER_URL      = "https://100067.connect.garena.com/api/v2/oauth/guest:register"
    TOKEN_URL         = "https://100067.connect.garena.com/api/v2/oauth/guest/token:grant"
    MAJOR_REGISTER_URL = "https://loginbp.ggpolarbear.com/MajorRegister"
    MAJOR_LOGIN_URL    = "https://loginbp.ggpolarbear.com/MajorLogin"
    # ──────────────────────────────────────────────────────────────────────────

    CURRENT_DIR            = os.path.dirname(os.path.abspath(__file__))
    BASE_FOLDER            = os.path.join(CURRENT_DIR, "AriyanxGUEST-GEN")
    TOKENS_FOLDER          = os.path.join(BASE_FOLDER, "TOKENS")
    ACCOUNTS_FOLDER        = os.path.join(BASE_FOLDER, "ACCOUNTS")
    RARE_ACCOUNTS_FOLDER   = os.path.join(BASE_FOLDER, "RARE_ACCOUNTS")
    COUPLES_ACCOUNTS_FOLDER= os.path.join(BASE_FOLDER, "COUPLES_ACCOUNTS")
    GHOST_FOLDER           = os.path.join(BASE_FOLDER, "GHOST")
    GHOST_ACCOUNTS_FOLDER  = os.path.join(GHOST_FOLDER, "ACCOUNTS")
    GHOST_RARE_FOLDER      = os.path.join(GHOST_FOLDER, "RARE_ACCOUNTS")
    GHOST_COUPLES_FOLDER   = os.path.join(GHOST_FOLDER, "COUPLES_ACCOUNTS")
    ACTIVATED_FOLDER       = os.path.join(BASE_FOLDER, "ACTIVATED")
    FAILED_ACTIVATION_FOLDER = os.path.join(BASE_FOLDER, "FAILED_ACTIVATION")
    CONFIG_FOLDER          = os.path.join(BASE_FOLDER, "CONFIG")
    BACKUP_FOLDER          = os.path.join(BASE_FOLDER, "BACKUP")

    @classmethod
    def create_folders(cls):
        folders = [
            cls.BASE_FOLDER, cls.TOKENS_FOLDER, cls.ACCOUNTS_FOLDER,
            cls.RARE_ACCOUNTS_FOLDER, cls.COUPLES_ACCOUNTS_FOLDER,
            cls.GHOST_FOLDER, cls.GHOST_ACCOUNTS_FOLDER, cls.GHOST_RARE_FOLDER,
            cls.GHOST_COUPLES_FOLDER, cls.ACTIVATED_FOLDER,
            cls.FAILED_ACTIVATION_FOLDER, cls.CONFIG_FOLDER, cls.BACKUP_FOLDER
        ]
        print(f"{VISUAL.COLORS['info']}📁 Initializing workspace directory map...{VISUAL.COLORS['reset']}")
        for folder in folders:
            os.makedirs(folder, exist_ok=True)
        print(f"{VISUAL.COLORS['success']}✅ Workspace directories loaded!{VISUAL.COLORS['reset']}")
        time.sleep(1)

# =============================================================================
# 🎭 REGION SERVER MAP FOR EMOTE EQUIPMENT (FROM 1.py)
# =============================================================================

REGION_SERVER_MAP = {
    "BD": "https://clientbp.ggpolarbear.com",
    "IND": "https://client.ind.freefiremobile.com",
    "PK": "https://clientbp.ggpolarbear.com",
    "ME": "https://clientbp.ggpolarbear.com",
    "VN": "https://clientbp.ggpolarbear.com",
    "SG": "https://clientbp.ggpolarbear.com",
    "ID": "https://clientbp.ggpolarbear.com",
    "TH": "https://clientbp.ggpolarbear.com",
    "BR": "https://client.us.freefiremobile.com",
    "NA": "https://client.us.freefiremobile.com",
    "US": "https://client.us.freefiremobile.com",
    "RU": "https://clientbp.ggpolarbear.com",
}

# =============================================================================
# 🗃️ SPECIAL BLOCK FONT DATA & PREMIUM BIO COLORS
# =============================================================================

BLOCK_FONT = {
    'A': ['░█▀█', '░█▀█', '░▀░▀'],
    'B': ['░█▀▄', '░█▀▄', '░▀▀░'],
    'C': ['░█▀▀', '░█░░', '░▀▀▀'],
    'D': ['░█▀▄', '░█░█', '░▀▀░'],
    'E': ['░█▀▀', '░█▀▀', '░▀▀▀'],
    'F': ['░█▀▀', '░█▀▀', '░▀░░'],
    'G': ['░█▀▀', '░█░█', '░▀▀▀'],
    'H': ['░█░█', '░█▀█', '░▀░▀'],
    'I': ['░▀█▀', '░░█░', '░▀▀▀'],
    'J': ['░░░█', '░░░█', '░▀▀░'],
    'K': ['░█░█', '░█▀▄', '░▀░▀'],
    'L': ['░█░░', '░█░░', '░▀▀▀'],
    'M': ['░█▄█', '░█░█', '░▀░▀'],
    'N': ['░█▀█', '░█░█', '░▀░▀'],
    'O': ['░█▀█', '░█░█', '░▀▀▀'],
    'P': ['░█▀█', '░█▀▀', '░▀░░'],
    'Q': ['░█▀█', '░█▄█', '░▀▀▀'],
    'R': ['░█▀▄', '░█▀▄', '░▀░▀'],
    'S': ['░█▀▀', '░▀▀█', '░▀▀▀'],
    'T': ['░▀█▀', '░░█░', '░░█░'],
    'U': ['░█░█', '░█░█', '░▀▀▀'],
    'V': ['░█░█', '░█░█', '░░▀░'],
    'W': ['░█░█', '░█▄█', '░▀░▀'],
    'X': ['░█░█', '░░█░', '░▀░▀'],
    'Y': ['░█░█', '░░█░', '░░▀░'],
    'Z': ['░▀▀█', '░░█░', '░▀▀▀'],
    ' ': ['░░░░', '░░░░', '░░░░']
}

BIO_COLORS = [
    "FF0000", "00FF00", "0000FF", "FFFF00", "A52A2A", 
    "FF00FF", "808080", "FF1493", "FFA500", "FFD700", "FFFFFF", 
    "C0C0C0", "482B10", "808000", "0F7209", "CCFF00", "00FFFF", 
    "00008B", "ADD8E6", "008000", "7FFFD4", "800000", "FFC0CB", 
    "FFD3EF", "6E00FF", "BF00FF"
]

def garena_bio_to_terminal(bio_text):
    """Parses Garena [RRGGBB] hex syntax into TrueColor escape sequences for console rendering"""
    C = VISUAL.COLORS
    def repl(match):
        hex_color = match.group(1)
        r = int(hex_color[0:2], 16)
        g = int(hex_color[2:4], 16)
        b = int(hex_color[4:6], 16)
        return f"\033[38;2;{r};{g};{b}m"
    colored_text = re.sub(r'\[([0-9A-Fa-f]{6})\]', repl, bio_text)
    return colored_text + C['reset']

# =============================================================================
# 🔑 ACCOUNT GENERATION HELPERS
# =============================================================================

def generate_exponent_number():
    exponent_digits = {'0': '⁰','1': '¹','2': '²','3': '³','4': '⁴',
                       '5': '⁵','6': '⁶','7': '⁷','8': '⁸','9': '⁹'}
    number = random.randint(1, 99999)
    return ''.join(exponent_digits[d] for d in f"{number:05d}")

def generate_random_name():
    base = Config.CUSTOM_NAME_PREFIX if Config.CUSTOM_NAME_PREFIX else "Ariyan"
    designs = [
        '▲','ℳ','☆','°','ℛ','『','ツ',
        '◇','༺','◆','웃','꧁','彡','★','ン',
        '•','乂','⍤','유','ヅ','Ø','♪','Ƹ','⌂','シ','⊹',
        '·','∞','♡','✦','✧','◈','▸','꧂','༻','࿐',
        'ʜ','ɪ','深度','ᴋ','ᴍ','ɴ','ꪆ','ꪀ','』','「','」',
        '〖','〗','【','】','《','》','ッ','জ','ヅ','亗',
        'ℳ','ℛ','Ɽ','Ƈ','Ƨ','Ƴ','Ʀ','Ƶ','⋆','⋈',
    ]
    designs = list(dict.fromkeys(designs))
    count = random.randint(3, 4)
    suffix = ''.join(random.choices(designs, k=count))
    return f"{base}{suffix}"

def generate_custom_password():
    prefix = Config.CUSTOM_PASS_PREFIX if Config.CUSTOM_PASS_PREFIX else "Ariyan"
    clean_prefix = ''.join(c for c in prefix if c.isalnum() or c == '_')
    if not clean_prefix:
        clean_prefix = "Ariyan"
    random_part = ''.join(random.choices(string.ascii_letters + string.digits, k=12))
    password = f"{clean_prefix}_ARIYAN_{random_part}"
    if len(password) > 64:
        password = password[:64]
    return password

def smart_delay():
    time.sleep(random.uniform(0.01, 0.05))

def encode_string(original):
    keystream = [0x30,0x30,0x30,0x32,0x30,0x31,0x37,0x30,0x30,0x30,0x30,0x30,0x32,0x30,0x31,0x37,
                 0x30,0x30,0x30,0x30,0x30,0x32,0x30,0x31,0x37,0x30,0x30,0x30,0x30,0x30,0x32,0x30]
    encoded = ""
    for i in range(len(original)):
        encoded += chr(ord(original[i]) ^ keystream[i % len(keystream)])
    return {"open_id": original, "field_14": encoded}

def to_unicode_escaped(s):
    return ''.join(c if 32 <= ord(c) <= 126 else '\\u{:04x}'.format(ord(c)) for c in s)

def decode_jwt_token(jwt_token):
    try:
        parts = jwt_token.split('.')
        if len(parts) >= 2:
            payload_part = parts[1]
            padding = 4 - len(payload_part) % 4
            if padding != 4:
                payload_part += '=' * padding
            decoded = base64.urlsafe_b64decode(payload_part)
            data = json.loads(decoded)
            account_id = data.get('account_id') or data.get('external_id')
            if account_id:
                return str(account_id)
    except:
        pass
    return "N/A"

# =============================================================================
# 🔐 ASYNC PROTOBUF HELPERS (OB54 working build)
# =============================================================================

async def EnC_Vr(N):
    if N < 0: return b''
    H = []
    while True:
        BesTo = N & 0x7F
        N >>= 7
        if N: BesTo |= 0x80
        H.append(BesTo)
        if not N: break
    return bytes(H)

async def CrEaTe_VarianT(field_number, value):
    return await EnC_Vr((field_number << 3) | 0) + await EnC_Vr(value)

async def CrEaTe_LenGTh(field_number, value):
    h = await EnC_Vr((field_number << 3) | 2)
    e = value.encode() if isinstance(value, str) else value
    return h + await EnC_Vr(len(e)) + e

async def CrEaTe_ProTo(fields):
    p = bytearray()
    for f, v in fields.items():
        if isinstance(v, dict):
            p.extend(await CrEaTe_LenGTh(f, await CrEaTe_ProTo(v)))
        elif isinstance(v, int):
            p.extend(await CrEaTe_VarianT(f, v))
        elif isinstance(v, (str, bytes)):
            p.extend(await CrEaTe_LenGTh(f, v))
    return p

def run_async(coro):
    loop = asyncio.new_event_loop()
    try:
        return loop.run_until_complete(coro)
    finally:
        loop.close()

def E_AEs(Pc):
    if not AES_AVAILABLE:
        return bytes.fromhex(Pc) if isinstance(Pc, str) else Pc
    Z = bytes.fromhex(Pc) if isinstance(Pc, str) else Pc
    key = bytes([89,103,38,116,99,37,68,69,117,104,54,37,90,99,94,56])
    iv  = bytes([54,111,121,90,68,114,50,50,69,51,121,99,104,106,77,37])
    K = AES.new(key, AES.MODE_CBC, iv)
    return K.encrypt(pad(Z, AES.block_size))

def encrypt_api(plain_text):
    if not AES_AVAILABLE:
        return plain_text
    Z = bytes.fromhex(plain_text)
    key = bytes([89,103,38,116,99,37,68,69,117,104,54,37,90,99,94,56])
    iv  = bytes([54,111,121,90,68,114,50,50,69,51,121,99,104,106,77,37])
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return cipher.encrypt(pad(Z, AES.block_size)).hex()

# =============================================================================
# 🔌 API MASTER  (OB54 — /api/v2/ JSON endpoints)
# =============================================================================

class APIMaster:
    HEX_KEY  = Config.HEX_KEY
    API_KEY  = Config.API_KEY
    API_POOL = [{"id": "100067", "key": Config.API_KEY, "label": f"API {i:02d} ⚡"} for i in range(1, 8)]

    @classmethod
    def init(cls):
        more_ids = ["100068","100069","100070","100071","100072"]
        for i, api_id in enumerate(more_ids, start=len(cls.API_POOL)+1):
            cls.API_POOL.append({"id": api_id, "key": cls.API_KEY, "label": f"API {i:02d} ⚡"})
        return len(cls.API_POOL)

API_COUNT = APIMaster.init()

# =============================================================================
# 📝 CREDIT EDITOR (ADMIN ONLY)
# =============================================================================

class CreditEditor:
    CREDIT_FILE = os.path.join(Config.CONFIG_FOLDER, "credit_config.json")

    @classmethod
    def load_credits(cls):
        default_credits = {
            "primary_credit": "Ariyan",
            "github": "https://github.com/Ariyan",
            "telegram1": "@Ariyan",
            "telegram2": "@Ariyan",
            "display_name": "Ariyan",
            "banner_text": "⚡ POWERED BY ARIYAN ⚡",
            "footer_text": "👤 CREDIT: Ariyan | TELEGRAM: @Ariyan,@Ariyan | GITHUB: Ariyan",
            "bio_text": "[FF0000]🌈[FF7700]A[FFFF00]R[00FF00]I[00BFFF]Y[8B00FF]A[FF0000]N[FFFF00]_[00FF00]C[00BFFF]O[8B00FF]D[FF0000]E [FF7700]C[FFFF00]R[00FF00]E[00BFFF]A[8B00FF]T[FF0000]I[FF7700]O[FFFF00]N[FF0000]🌈",
            "last_modified": datetime.now().isoformat(),
            "modified_by": Config.USER_LEVEL
        }
        try:
            if os.path.exists(cls.CREDIT_FILE):
                with open(cls.CREDIT_FILE, 'r') as f:
                    return json.load(f)
            else:
                cls.save_credits(default_credits)
                return default_credits
        except:
            return default_credits

    @classmethod
    def save_credits(cls, credits):
        try:
            credits["last_modified"] = datetime.now().isoformat()
            credits["modified_by"] = Config.USER_LEVEL
            os.makedirs(os.path.dirname(cls.CREDIT_FILE), exist_ok=True)
            with open(cls.CREDIT_FILE, 'w') as f:
                json.dump(credits, f, indent=4)
            return True
        except:
            return False

    @classmethod
    def backup_current_file(cls):
        try:
            backup_name = f"backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.py"
            backup_path = os.path.join(Config.BACKUP_FOLDER, backup_name)
            shutil.copy2(__file__, backup_path)
            return backup_path
        except:
            return None

# =============================================================================
# 🔐 FILE LOCK / JSON
# =============================================================================

def get_file_lock(filename):
    if filename not in Config.FILE_LOCKS:
        Config.FILE_LOCKS[filename] = threading.Lock()
    return Config.FILE_LOCKS[filename]

def safe_json_save(filepath, data):
    try:
        parent = os.path.dirname(filepath)
        if parent and not os.path.isdir(parent):
            os.makedirs(parent, exist_ok=True)
        temp = filepath + '.tmp'
        with open(temp, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)
        os.replace(temp, filepath) if os.path.exists(filepath) else os.rename(temp, filepath)
        return True
    except:
        return False

def safe_json_load(filepath, default=None):
    try:
        if os.path.isfile(filepath):
            with open(filepath, 'r', encoding='utf-8') as f:
                return json.load(f)
    except:
        pass
    return default if default is not None else []

# =============================================================================
# 🔄 COUPLES DETECTION
# =============================================================================

POTENTIAL_COUPLES = {}
COUPLES_LOCK = threading.Lock()

# =============================================================================
# 🚦 SIGNAL HANDLING
# =============================================================================

EXIT_FLAG = False

def safe_exit(signum=None, frame=None):
    global EXIT_FLAG
    EXIT_FLAG = True
    print(f"\n{VISUAL.COLORS['warning']}🚨 Ariyan system shutting down immediately...{VISUAL.COLORS['reset']}")
    sys.exit(0)

signal.signal(signal.SIGINT, safe_exit)
signal.signal(signal.SIGTERM, safe_exit)

# =============================================================================
# 🖨️ PRINT FUNCTIONS
# =============================================================================

C = VISUAL.COLORS

GENERATION_SILENT = False

def print_success(msg):
    if not GENERATION_SILENT: print(f"{C['success']}{C['bold']}✅ {msg}{C['reset']}")
def print_error(msg):
    if not GENERATION_SILENT: print(f"{C['error']}{C['bold']}❌ {msg}{C['reset']}")
def print_warning(msg):
    if not GENERATION_SILENT: print(f"{C['warning']}{C['bold']}⚠️  {msg}{C['reset']}")
def print_info(msg):
    if not GENERATION_SILENT: print(f"{C['info']}💡  {msg}{C['reset']}")
def print_rare(msg):
    if not GENERATION_SILENT: print(f"{C['rare']}{C['bold']}💎 {msg}{C['reset']}")
def print_couple(msg):
    if not GENERATION_SILENT: print(f"{C['couple']}{C['bold']}💞 {msg}{C['reset']}")
def print_activation(msg):
    if not GENERATION_SILENT: print(f"{C['primary']}{C['bold']}🔥 {msg}{C['reset']}")

def debug_print(msg):
    if not GENERATION_SILENT and Config.USER_LEVEL in ["ADMIN","OWNER"] and Config.DEBUG_MODE:
        print(f"{C['dim']}🔍 DEBUG: {msg}{C['reset']}")

# =============================================================================
# 🔐 DYNAMIC PROTOBUF DEFINITION FOR BIODATA (from aa.py / m.py)
# =============================================================================
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

_sym_db = _symbol_database.Default()
try:
    DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
        b'\n\ndata.proto\"\xbb\x01\n\x04\x44\x61ta\x12\x0f\n\x07\x66ield_2\x18\x02 \x01(\x05\x12\x1e\n\x07\x66ield_5\x18\x05 \x01(\x0b\x32\r.EmptyMessage\x12\x1e\n\x07\x66ield_6\x18\x06 \x01(\x0b\x32\r.EmptyMessage\x12\x0f\n\x07\x66ield_8\x18\x08 \x01(\t\x12\x0f\n\x07\x66ield_9\x18\t \x01(\x05\x12\x1f\n\x08\x66ield_11\x18\x0b \x01(\x0b\x32\r.EmptyMessage\x12\x1f\n\x08\x66ield_12\x18\x0c \x01(\x0b\x32\r.EmptyMessage\"\x0e\n\x0c\x45mptyMessageb\x06proto3'
    )
    _globals = globals()
    _builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
    _builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'data1_pb2', _globals)
    BioData = _sym_db.GetSymbol('Data')
    EmptyMessage = _sym_db.GetSymbol('EmptyMessage')
    BIO_PROTO_AVAILABLE = True
except Exception as _bio_ex:
    BIO_PROTO_AVAILABLE = False

BIO_SET_COUNTER = 0

_BIO_HEADERS = {
    "Expect":          "100-continue",
    "X-Unity-Version": "2018.4.11f1",
    "X-GA":            "v1 1",
    "ReleaseVersion":  "OB54",
    "Content-Type":    "application/x-www-form-urlencoded",
    "User-Agent":      "Dalvik/2.1.0 (Linux; U; Android 11; SM-A305F Build/RP1A.200720.012)",
    "Connection":      "Keep-Alive",
    "Accept-Encoding": "gzip",
}

_BIO_AES_KEY = bytes([89,103,38,116,99,37,68,69,117,104,54,37,90,99,94,56])
_BIO_AES_IV  = bytes([54,111,121,90,68,114,50,50,69,51,121,99,104,106,77,37])

def _bio_encrypt(data_bytes):
    if not AES_AVAILABLE:
        return data_bytes
    from Crypto.Cipher import AES as _AES
    from Crypto.Util.Padding import pad as _pad
    cipher = _AES.new(_BIO_AES_KEY, _AES.MODE_CBC, _BIO_AES_IV)
    return cipher.encrypt(_pad(data_bytes, _AES.block_size))

def _bio_guest_login(uid, password):
    try:
        payload = {
            'uid':           str(uid),
            'password':      str(password),
            'response_type': 'token',
            'client_type':   '2',
            'client_secret': Config.HEX_KEY,
            'client_id':     '100067',
        }
        headers = {'User-Agent': 'GarenaMSDK/4.0.19P9(SM-M526B ;Android 13;pt;BR;)',
                   'Connection': 'Keep-Alive'}
        resp = requests.post(
            'https://100067.connect.garena.com/oauth/guest/token/grant',
            data=payload, headers=headers, timeout=10, verify=False
        )
        data = resp.json()
        return data.get('access_token'), data.get('open_id')
    except:
        return None, None

def _bio_update(jwt_token, bio_text, base_url):
    if not BIO_PROTO_AVAILABLE:
        return False
    try:
        if not base_url:
            return False
        url = f"{base_url}/UpdateSocialBasicInfo"
        data = BioData()
        data.field_2 = 17
        data.field_5.CopyFrom(EmptyMessage())
        data.field_6.CopyFrom(EmptyMessage())
        data.field_8 = bio_text
        data.field_9 = 1
        data.field_11.CopyFrom(EmptyMessage())
        data.field_12.CopyFrom(EmptyMessage())

        encrypted = _bio_encrypt(data.SerializeToString())
        headers = _BIO_HEADERS.copy()
        headers['Authorization'] = f'Bearer {jwt_token}'
        r = requests.post(url, headers=headers, data=encrypted, verify=False, timeout=10)
        return r.status_code == 200
    except:
        return False

def set_account_bio(uid, password, bio_text, region="IND", existing_jwt=None, base_url=None):
    global BIO_SET_COUNTER
    if not Config.AUTO_BIO:
        return False
    try:
        bio_to_use = bio_text
        jwt_token  = existing_jwt

        if not jwt_token or not base_url:
            debug_print(f"Bio: full login required for uid={uid}")
            access_token, open_id = _bio_guest_login(uid, password)
            if not access_token or not open_id:
                debug_print("Bio: guest login failed")
                return False

            sess = requests.Session()
            login_result = _perform_major_login_sync(
                uid, password, access_token, open_id, region, sess
            )
            jwt_token = login_result.get("jwt_token", "")
            base_url  = login_result.get("ml_url", "")

        if not jwt_token or not base_url:
            debug_print("Bio: could not obtain dynamic JWT or Base URL")
            return False

        debug_print(f"Bio: updating bio dynamically for uid={uid} on {base_url}")
        success = _bio_update(jwt_token, bio_to_use, base_url)
        if success:
            with Config.LOCK:
                BIO_SET_COUNTER += 1
            return True
        else:
            debug_print(f"Bio: update request failed for uid={uid}")
    except Exception as e:
        debug_print(f"Bio error: {e}")
    return False

# =============================================================================
# 💎 RARITY DETECTION
# =============================================================================

ACCOUNT_RARITY_PATTERNS = {
    "REPEATED_DIGITS_4":       [r"(\d)\1{3,}", 3],
    "REPEATED_DIGITS_3":       [r"(\d)\1\1(\d)\2\2", 2],
    "SEQUENTIAL_5":            [r"(12345|23456|34567|45678|56789)", 4],
    "SEQUENTIAL_4":            [r"(0123|1234|2345|3456|4567|45678|5678|6789|9876|8765|7654|6543|5432|4321|3210)", 3],
    "PALINDROME_6":            [r"^(\d)(\d)(\d)\3\2\1$", 5],
    "PALINDROME_4":            [r"^(\d)(\d)\2\1$", 3],
    "SPECIAL_COMBINATIONS_HIGH":[r"(69|420|1337|007)", 4],
    "SPECIAL_COMBINATIONS_MED": [r"(100|200|300|400|500|666|777|888|999)", 2],
    "QUADRUPLE_DIGITS":        [r"(1111|2222|3333|4444|5555|6666|7777|8888|9999|0000)", 4],
    "MIRROR_PATTERN_HIGH":     [r"^(\d{2,3})\1$", 3],
    "MIRROR_PATTERN_MED":      [r"(\d{2})0\1", 2],
    "GOLDEN_RATIO":            [r"1618|0618", 3],
}

def check_account_rarity(account_data):
    account_id = account_data.get("account_id", "")
    if account_id == "N/A" or not account_id:
        return False, None, None, 0
    rarity_score = 0
    detected_patterns = []
    for rarity_type, pattern_data in ACCOUNT_RARITY_PATTERNS.items():
        if re.search(pattern_data[0], account_id):
            rarity_score += pattern_data[1]
            detected_patterns.append(rarity_type)
    digits = [int(d) for d in account_id if d.isdigit()]
    if len(set(digits)) == 1 and len(digits) >= 4:
        rarity_score += 5; detected_patterns.append("UNIFORM_DIGITS")
    if len(digits) >= 4:
        diffs = [digits[i+1] - digits[i] for i in range(len(digits)-1)]
        if len(set(diffs)) == 1:
            rarity_score += 4; detected_patterns.append("ARITHMETIC_SEQUENCE")
    if len(account_id) <= 8 and account_id.isdigit() and int(account_id) < 1000000:
        rarity_score += 3; detected_patterns.append("LOW_ACCOUNT_ID")
    threshold = Config.CUSTOM_RARITY_THRESHOLD if Config.USER_LEVEL in ["ADMIN","OWNER"] else Config.RARITY_THRESHOLD
    if rarity_score >= threshold:
        reason = f"ID {account_id} — Score: {rarity_score} — Patterns: {', '.join(detected_patterns)}"
        return True, "RARE_ACCOUNT", reason, rarity_score
    return False, None, None, rarity_score

def check_account_couples(account_data, thread_id):
    account_id = account_data.get("account_id", "")
    if account_id == "N/A" or not account_id:
        return False, None, None
    with COUPLES_LOCK:
        for stored_id, stored_data in list(POTENTIAL_COUPLES.items()):
            couple_found, reason = check_account_couple_patterns(account_id, stored_data.get('account_id', ''))
            if couple_found:
                partner_data = stored_data
                del POTENTIAL_COUPLES[stored_id]
                return True, reason, partner_data
        POTENTIAL_COUPLES[account_id] = {
            'uid': account_data.get('uid',''), 'account_id': account_id,
            'name': account_data.get('name',''), 'password': account_data.get('password',''),
            'region': account_data.get('region',''), 'thread_id': thread_id,
            'timestamp': datetime.now().isoformat()
        }
    return False, None, None

def check_account_couple_patterns(a1, a2):
    if a1 and a2 and abs(int(a1) - int(a2)) == 1:
        return True, f"Sequential IDs: {a1} & {a2}"
    if a1 == a2[::-1]:
        return True, f"Mirror IDs: {a1} & {a2}"
    if a1 and a2:
        s = int(a1) + int(a2)
        if s % 1000 == 0 or s % 10000 == 0:
            return True, f"Complementary sum: {a1}+{a2}={s}"
    for ln in ['520','521','1314','3344']:
        if ln in a1 and ln in a2:
            return True, f"Both contain love number: {ln}"
    return False, None

def print_rarity_found(account_data, rarity_type, reason, rarity_score):
    import sys, time
    RED  = '\033[38;5;201m'
    RED2 = '\033[38;5;165m'
    B = VISUAL.COLORS['bold']; R = VISUAL.COLORS['reset']
    W = 54
    for _ in range(4):
        for ch in ['░','▒','▓','█','▓','▒']:
            sys.stdout.write(f"\r{RED}{B}╔" + ch*W + f"╗{R}")
            sys.stdout.flush(); time.sleep(0.010)
    print()
    print(f"{RED}{B}╔{'═'*W}╗{R}")
    print(f"{RED}{B}║{'💎  RARE ACCOUNT DETECTED!  💎'.center(W)}║{R}")
    print(f"{RED}{B}╠{'═'*W}╣{R}")
    def row(k, v):
        line = f"  {k}: {v}"
        pad  = max(0, W - len(line) - 1)
        print(f"{RED}{B}║{R}  {RED2}{k}{R}: {RED}{B}{v}{R}{' '*pad}{RED}{B}║{R}")
    row("?? Category ", str(rarity_type))
    row("⭐ Matrix Sc", str(rarity_score))
    row("👤 Identity ", account_data['name'])
    row("🆔 UID Code ", str(account_data['uid']))
    row("🎮 Game ID  ", account_data.get('account_id', 'N/A'))
    row("📝 Reason   ", str(reason)[:45])
    print(f"{RED}{B}╠{'═'*W}╣{R}")
    print(f"{RED}{B}║{'🌌  SAVED TO RARE ARCHIVES  🌌'.center(W)}║{R}")
    print(f"{RED}{B}╚{'═'*W}╝{R}\n")

def print_couples_found(account1, account2, reason):
    import sys, time
    GRN  = '\033[38;5;51m'
    GRN2 = '\033[38;5;45m'
    GRN3 = '\033[38;5;39m'
    B = VISUAL.COLORS['bold']; R = VISUAL.COLORS['reset']
    W = 58
    for ch in ['·','◇','◈','═']:
        sys.stdout.write(f"\r{GRN}{B}╔" + ch*W + f"╗{R}")
        sys.stdout.flush(); time.sleep(0.022)
    print()
    print(f"{GRN}{B}╔{'═'*W}╗{R}")
    print(f"{GRN}{B}║{'💞  COUPLES MATCH FOUND!  💞'.center(W)}║{R}")
    print(f"{GRN}{B}╠{'═'*W}╣{R}")
    def row(k, v):
        line = f"  {k}: {v}"
        pad  = max(0, W - len(line) - 1)
        print(f"{GRN}{B}║{R}  {GRN3}{k}{R}: {GRN}{B}{v}{R}{' '*pad}{GRN}{B}║{R}")
    row("📝 Reason   ", str(reason))
    print(f"{GRN}{B}╠{'─'*W}╣{R}")
    print(f"{GRN}{B}║{'  ACCOUNT  1  '.center(W)}║{R}")
    row("👤 Name     ", account1['name'])
    row("🆔 UID      ", str(account1.get('uid','N/A')))
    row("🎮 Game ID  ", account1.get('account_id','N/A'))
    print(f"{GRN}{B}╠{'─'*W}╣{R}")
    print(f"{GRN}{B}║{'  ACCOUNT  2  '.center(W)}║{R}")
    row("👤 Name     ", account2['name'])
    row("🆔 UID      ", str(account2.get('uid','N/A')))
    row("🎮 Game ID  ", account2.get('account_id','N/A'))
    print(f"{GRN}{B}╠{'═'*W}╣{R}")
    print(f"{GRN}{B}║{'💜  SAVED TO COUPLES REGISTRY  💜'.center(W)}║{R}")
    print(f"{GRN}{B}╚{'═'*W}╝{R}\n")

# =============================================================================
# ⚡ AUTO ACTIVATOR
# =============================================================================

class AutoActivator:
    def __init__(self, max_workers=16, turbo_mode=True):
        self.key = bytes([89, 103, 38, 116, 99, 37, 68, 69, 117, 104, 54, 37, 90, 99, 94, 56])
        self.iv  = bytes([54, 111, 121, 90, 68, 114, 50, 50, 69, 51, 121, 99, 104, 106, 77, 37])
        self.max_workers    = max_workers
        self.turbo_mode     = turbo_mode
        self.stop_execution = False
        self.stats_lock     = threading.Lock()
        self.unauthorized_count = 0
        self.max_unauthorized_before_stop = 15

        self.session  = requests.Session()
        self.adapters = self._create_optimized_adapters()
        self._rotate_adapter()

    def _create_optimized_adapters(self):
        configs = [
            {'pool_connections': 100, 'pool_maxsize': 100, 'max_retries': 1},
            {'pool_connections': 50,  'pool_maxsize': 50,  'max_retries': 0},
            {'pool_connections': 75,  'pool_maxsize': 75,  'max_retries': 2},
        ]
        return [requests.adapters.HTTPAdapter(**c) for c in configs]

    def _rotate_adapter(self):
        adapter = random.choice(self.adapters)
        self.session.mount('http://',  adapter)
        self.session.mount('https://', adapter)

    def generate_fingerprint(self):
        user_agents = [
            'Dalvik/2.1.0 (Linux; U; Android 9; ASUS_Z01QD Build/PI)',
            'Dalvik/2.1.0 (Linux; U; Android 10; SM-G973F Build/QP1A.190711.020)',
            'Dalvik/2.1.0 (Linux; U; Android 11; Pixel 5 Build/RQ3A.210805.001)',
            'Dalvik/2.1.0 (Linux; U; Android 12; SM-A525F Build/SP1A.210812.016)',
            'Dalvik/2.1.0 (Linux; U; Android 13; Redmi Note 12 Build/TKQ1.220829.002)',
            'Mozilla/5.0 (Linux; Android 11; SM-G991B) AppleWebKit/537.36 Chrome/91 Mobile Safari/537.36',
            'Mozilla/5.0 (Linux; Android 10; Pixel 4) AppleWebKit/537.36 Chrome/92 Mobile Safari/537.36',
        ]
        self.session.headers.update({
            'User-Agent': random.choice(user_agents),
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive',
            'Cache-Control': 'no-cache',
        })
        self._rotate_adapter()

    def smart_rate_limit_bypass(self):
        delay = random.uniform(0.03, 0.12) if self.turbo_mode else random.uniform(0.1, 0.25)
        time.sleep(delay)
        self.generate_fingerprint()

    def advanced_retry_strategy(self, attempt, max_attempts=3):
        base  = 1.5 ** attempt if self.turbo_mode else 2 ** attempt
        delay = base * random.uniform(0.8, 1.5)
        time.sleep(min(delay, 8.0))

    def encrypt_api(self, plain_text):
        if not AES_AVAILABLE:
            return plain_text
        try:
            plain_text = bytes.fromhex(plain_text)
            cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
            return cipher.encrypt(pad(plain_text, AES.block_size)).hex()
        except:
            return None

    def parse_my_message(self, serialized_data):
        try:
            import MajorLoginRes_pb2 as _mlr
            msg = _mlr.MajorLoginRes()
            msg.ParseFromString(serialized_data)
            jwt   = msg.token
            key_h = msg.ak.hex()  if msg.ak  else None
            iv_h  = msg.aiv.hex() if msg.aiv else None
            if jwt:
                return jwt, key_h, iv_h
        except Exception:
            pass

        if NEW_PROTO_AVAILABLE:
            try:
                res = MajoRLoGinrEs_pb2.MajorLoginRes()
                res.ParseFromString(serialized_data)
                if res.token:
                    key_b = bytes(res.ak)  if res.ak  else None
                    iv_b  = bytes(res.aiv) if res.aiv else None
                    return res.token, (key_b.hex() if key_b else None), (iv_b.hex() if iv_b else None)
            except Exception:
                pass

        try:
            text = serialized_data.decode('utf-8', errors='ignore')
            jwt_start = text.find("eyJ")
            if jwt_start != -1:
                jwt_token = text[jwt_start:]
                second_dot = jwt_token.find(".", jwt_token.find(".") + 1)
                if second_dot != -1:
                    return jwt_token[:second_dot + 44], None, None
        except Exception:
            pass

        return None, None, None

    def guest_token(self, uid, password, region='IND'):
        if self.stop_execution:
            return None, None
        region_config = Config.ACTIVATION_REGIONS.get(region, Config.ACTIVATION_REGIONS['IND'])
        url = region_config['guest_url']
        data = {
            "uid": f"{uid}", "password": f"{password}",
            "response_type": "token", "client_type": "2",
            "client_secret": Config.HEX_KEY, "client_id": "100067",
        }
        max_attempts = 4 if self.turbo_mode else 3
        for attempt in range(max_attempts):
            try:
                if self.stop_execution:
                    return None, None
                self.smart_rate_limit_bypass()
                timeout = 8 if self.turbo_mode else 15
                response = self.session.post(url, data=data, timeout=timeout, verify=False)
                if response.status_code == 200:
                    d = response.json()
                    return d.get('access_token'), d.get('open_id')
                elif response.status_code == 429:
                    self.advanced_retry_strategy(attempt, max_attempts)
                    continue
                elif response.status_code in [400, 401, 403]:
                    if response.status_code == 401:
                        with self.stats_lock:
                            self.unauthorized_count += 1
                            if self.unauthorized_count >= self.max_unauthorized_before_stop:
                                self.stop_execution = True
                    return None, None
            except requests.exceptions.Timeout:
                pass
            except Exception:
                pass
            if attempt < max_attempts - 1:
                self.advanced_retry_strategy(attempt, max_attempts)
        return None, None

    def major_login(self, access_token, open_id, region='IND'):
        if self.stop_execution:
            return None
        region_config = Config.ACTIVATION_REGIONS.get(region, Config.ACTIVATION_REGIONS['IND'])
        url = region_config['major_login_url']

        headers = {
            'X-Unity-Version': '2018.4.11f1',
            'ReleaseVersion':  'OB54',
            'Content-Type':    'application/x-www-form-urlencoded',
            'X-GA':            'v1 1',
            'User-Agent':      'Dalvik/2.1.0 (Linux; U; Android 7.1.2; ASUS_Z01QD Build/QKQ1.190825.002)',
            'Host':            'loginbp.ggpolarbear.com',
            'Connection':      'Keep-Alive',
        }

        payload_template = bytes.fromhex(
            '1a13323032352d30372d33302031313a30323a3531220966726565206669726528013a07312e3131342e32422c416e64726f6964204f5320372e312e32202f204150492d323320284e32473438482f373030323530323234294a0848616e6468656c645207416e64726f69645a045749464960c00c68840772033332307a1f41524d7637205646507633204e454f4e20564d48207c2032343635207c203480019a1b8a010f416472656e6f2028544d292036343092010d4f70656e474c20455320332e319a012b476f6f676c657c31663361643662372d636562342d343934622d383730622d623164616364373230393131a2010c3139372e312e31322e313335aa0102656eb201203939366136323964626364623339363462653662363937386635643831346462ba010134c2010848616e6468656c64ca011073616d73756e6720534d2d473935354eea014066663930633037656239383135616633306134336234613966363031393531366530653463373033623434303932353136643064656661346365663531663261f00101ca0207416e64726f6964d2020457494649ca03203734323862323533646566633136343031386336303461316562626665626466e003daa907e803899b07f003bf0ff803ae088004999b078804daa9079004999b079804daa907c80403d204262f646174612f6170702f636f6d2e6474732e667265656669726574682d312f6c69622f626173652e61706bf00403f804018a050233329a050a32303139313138363933a80503b205094f70656e474c455332b805ff7fc00504e005dac901ea0507616e64726f6964f2055c4b71734854394748625876574c6668437950416c52526873626d43676542557562555551317375746d525536634e30524f3751453141486e496474385963784d614c575437636d4851322b7374745279377830663935542b6456593d8806019006019a060134a2060134b2061e40001147550d0c074f530b4d5c584d57416657545a065f2a091d6a0d5033'
        )
        OLD_OPEN_ID      = b"996a629dbcdb3964be6b6978f5d814db"
        OLD_ACCESS_TOKEN = b"ff90c07eb9815af30a43b4a9f6019516e0e4c703b44092516d0defa4cef51f2a"
        payload = payload_template.replace(OLD_OPEN_ID, open_id.encode())
        payload = payload.replace(OLD_ACCESS_TOKEN, access_token.encode())
        encrypted_payload = self.encrypt_api(payload.hex())
        if not encrypted_payload:
            return None
        final_payload = bytes.fromhex(encrypted_payload)

        max_attempts = 3
        for attempt in range(max_attempts):
            try:
                if self.stop_execution:
                    return None
                self.smart_rate_limit_bypass()
                timeout = 12 if self.turbo_mode else 18
                response = self.session.post(
                    url, headers=headers, data=final_payload,
                    verify=False, timeout=timeout
                )
                if response.status_code == 200 and len(response.content) > 0:
                    return response.content
                elif response.status_code == 429:
                    self.advanced_retry_strategy(attempt, max_attempts)
                    continue
            except Exception:
                pass
            if attempt < max_attempts - 1:
                self.advanced_retry_strategy(attempt, max_attempts)
        return None

    def GET_PAYLOAD_BY_DATA(self, JWT_TOKEN, NEW_ACCESS_TOKEN, region='IND'):
        try:
            token_payload_base64 = JWT_TOKEN.split('.')[1]
            token_payload_base64 += '=' * ((4 - len(token_payload_base64) % 4) % 4)
            decoded_payload = json.loads(base64.urlsafe_b64decode(token_payload_base64).decode('utf-8'))
            NEW_EXTERNAL_ID = decoded_payload['external_id']
            SIGNATURE_MD5   = decoded_payload['signature_md5']
            now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            payload = bytes.fromhex(
                "1a13323032352d30372d33302031313a30323a3531220966726565206669726528013a07312e3131342e32422c416e64726f6964204f5320372e312e32202f204150492d323320284e32473438482f373030323530323234294a0848616e6468656c645207416e64726f69645a045749464960c00c68840772033332307a1f41524d7637205646507633204e454f4e20564d48207c2032343635207c203480019a1b8a010f416472656e6f2028544d292036343092010d4f70656e474c20455320332e319a012b476f6f676c657c31663361643662372d636562342d343934622d383730622d623164616364373230393131a2010c3139372e312e31322e313335aa0102656eb201203939366136323964626364623339363462653662363937386635643831346462ba010134c2010848616e6468656c64ca011073616d73756e6720534d2d473935354eea014066663930633037656239383135616633306134336234613966363031393531366530653463373033623434303932353136643064656661346365663531663261f00101ca0207416e64726f6964d2020457494649ca03203734323862323533646566633136343031386336303461316562626665626466e003daa907e803899b07f003bf0ff803ae088004999b078804daa9079004999b079804daa907c80403d204262f646174612f6170702f636f6d2e6474732e667265656669726574682d312f6c69622f626173652e61706bf00403f804018a050233329a050a32303139313138363933a80503b205094f70656e474c455332b805ff7fc00504e005dac901ea0507616e64726f6964f2055c4b71734854394748625876574c6668437950416c52526873626d43676542557562555551317375746d525536634e30524f3751453141486e496474385963784d614c575437636d4851322b7374745279377830663935542b6456593d8806019006019a060134a2060134b2061e40001147550d0c074f530b4d5c584d57416657545a065f2a091d6a0d5033"
            )
            payload = payload.replace(b"2025-07-30 11:02:51", now.encode())
            payload = payload.replace(
                b"ff90c07eb9815af30a43b4a9f6019516e0e4c703b44092516d0defa4cef51f2a",
                NEW_ACCESS_TOKEN.encode("UTF-8")
            )
            payload = payload.replace(b"996a629dbcdb3964be6b6978f5d814db", NEW_EXTERNAL_ID.encode("UTF-8"))
            payload = payload.replace(b"7428b253defc164018c604a1ebbfebdf", SIGNATURE_MD5.encode("UTF-8"))
            PAYLOAD = self.encrypt_api(payload.hex())
            if PAYLOAD:
                return bytes.fromhex(PAYLOAD)
            return None
        except Exception as e:
            debug_print(f"GET_PAYLOAD_BY_DATA error: {e}")
            return None

    def GET_LOGIN_DATA(self, JWT_TOKEN, PAYLOAD, region='IND'):
        if self.stop_execution:
            return False
        region_config = Config.ACTIVATION_REGIONS.get(region, Config.ACTIVATION_REGIONS['IND'])
        url         = region_config['get_login_data_url']
        client_host = region_config['client_host']
        headers = {
            'Expect':        '100-continue',
            'Authorization': f'Bearer {JWT_TOKEN}',
            'X-Unity-Version': '2018.4.11f1',
            'X-GA':          'v1 1',
            'ReleaseVersion': 'OB54',
            'Content-Type':  'application/x-www-form-urlencoded',
            'User-Agent':    'Dalvik/2.1.0 (Linux; U; Android 9; G011A Build/PI)',
            'Host':          client_host,
            'Connection':    'close',
            'Accept-Encoding': 'gzip, deflate, br',
        }
        max_attempts = 2
        for attempt in range(max_attempts):
            try:
                if self.stop_execution:
                    return False
                self.smart_rate_limit_bypass()
                timeout = 8 if self.turbo_mode else 12
                response = self.session.post(
                    url, headers=headers, data=PAYLOAD,
                    verify=False, timeout=timeout
                )
                if response.status_code == 200:
                    return True
                elif response.status_code == 401:
                    with self.stats_lock:
                        self.unauthorized_count += 1
                        if self.unauthorized_count >= self.max_unauthorized_before_stop:
                            self.stop_execution = True
                    return False
                elif response.status_code == 404:
                    return False
            except Exception:
                pass
            if attempt < max_attempts - 1:
                self.advanced_retry_strategy(attempt, max_attempts)
        return False

    def activate_account(self, account_data):
        uid      = account_data['uid']
        password = account_data['password']
        region   = account_data.get('region', 'IND')
        if region not in Config.ACTIVATION_REGIONS:
            region = 'IND'

        access_token, open_id = self.guest_token(uid, password, region)
        if not access_token or not open_id:
            return False

        major_login_response = self.major_login(access_token, open_id, region)
        if not major_login_response:
            return False

        jwt_token, key, iv = self.parse_my_message(major_login_response)
        if not jwt_token:
            return False

        payload = self.GET_PAYLOAD_BY_DATA(jwt_token, access_token, region)
        if not payload:
            return False

        return self.GET_LOGIN_DATA(jwt_token, payload, region)

auto_activator = AutoActivator(max_workers=16, turbo_mode=True)

# =============================================================================
# 👤 ACCOUNT CREATION  (OB54 FIXED — new endpoints + JSON body)
# =============================================================================

def create_acc(region, session, is_ghost=False):
    if EXIT_FLAG:
        return None

    max_attempts = Config.MAX_RETRIES

    for attempt in range(max_attempts):
        try:
            password = generate_custom_password()

            # ── STEP 1: Register (/api/v2/ JSON body) ──────────────────────────
            payload_register = json.dumps(
                {"app_id": 100067, "client_type": 2, "password": password, "source": 2},
                separators=(',', ':')
            )
            signature = hmac.new(Config.API_KEY, payload_register.encode(), hashlib.sha256).hexdigest()
            headers_reg = {
                "User-Agent": "GarenaMSDK/4.0.39(SM-A325M ;Android 13;en;HK;)",
                "Authorization": f"Signature {signature}",
                "Content-Type": "application/json; charset=utf-8",
                "Accept": "application/json",
                "Connection": "Keep-Alive",
                "Host": "100067.connect.garena.com",
            }
            debug_print(f"Register attempt {attempt+1}")
            resp_reg = session.post(
                Config.REGISTER_URL,
                headers=headers_reg,
                data=payload_register,
                timeout=15,
                verify=False
            )
            if resp_reg.status_code != 200:
                if resp_reg.status_code == 429:
                    time.sleep(0.5)
                continue
            reg_json = resp_reg.json()
            if reg_json.get("code") != 0:
                debug_print(f"Register error code: {reg_json}")
                continue
            uid = reg_json['data']['uid']
            smart_delay()
            with Config.LOCK:
                Config.ATTEMPTS += 1

            # ── STEP 2: Token (/api/v2/ JSON body) ─────────────────────────────
            payload_token = json.dumps({
                "client_id": 100067,
                "client_secret": Config.HEX_KEY,
                "client_type": 2,
                "password": password,
                "response_type": "token",
                "uid": uid,
            }, separators=(',', ':'))
            signature2 = hmac.new(Config.API_KEY, payload_token.encode(), hashlib.sha256).hexdigest()
            headers_tok = {
                "User-Agent": "GarenaMSDK/4.0.39(SM-A325M ;Android 13;en;HK;)",
                "Authorization": f"Signature {signature2}",
                "Content-Type": "application/json; charset=utf-8",
                "Accept": "application/json",
                "Connection": "Keep-Alive",
                "Host": "100067.connect.garena.com",
            }
            resp_tok = session.post(
                Config.TOKEN_URL,
                headers=headers_tok,
                data=payload_token,
                timeout=15,
                verify=False
            )
            if resp_tok.status_code != 200:
                continue
            tok_json = resp_tok.json()
            if tok_json.get("code") != 0:
                debug_print(f"Token error: {tok_json}")
                continue
            access_token = tok_json['data']['access_token']
            open_id      = tok_json['data']['open_id']
            smart_delay()
            with Config.LOCK:
                Config.ATTEMPTS += 1

            # ── STEP 3: MajorRegister (ggpolarbear.com, sync) ────────────
            name = generate_random_name()
            api_config = {"id": "100067", "key": Config.API_KEY, "label": "API OB54 ⚡"}
            return _major_register_and_login_sync(
                uid, password, access_token, open_id, name,
                region, api_config, session, is_ghost
            )

        except Exception as e:
            debug_print(f"create_acc error: {str(e)[:50]}")

        smart_delay()

    return None

def _major_register_and_login_sync(uid, password, access_token, open_id, name,
                                    region, api_config, session, is_ghost):
    try:
        keystream = [0x30,0x30,0x30,0x32,0x30,0x31,0x37,0x30,0x30,0x30,0x30,0x30,0x32,0x30,0x31,0x37,
                     0x30,0x30,0x30,0x30,0x30,0x32,0x30,0x31,0x37,0x30,0x30,0x30,0x30,0x30,0x32,0x30]
        encoded_open_id = ""
        for i, ch in enumerate(open_id):
            encoded_open_id += chr(ord(ch) ^ keystream[i % len(keystream)])
        field14 = encoded_open_id.encode('latin1')

        lang_code = "pt" if is_ghost else Config.REGION_LANG.get(region.upper(), "en")
        payload_fields = {
            1: name, 2: access_token, 3: open_id,
            5: 102000007, 6: 4, 7: 1, 13: 1,
            14: field14, 15: lang_code, 16: 1, 17: 1
        }
        proto_bytes = run_async(CrEaTe_ProTo(payload_fields))
        encrypted_payload = E_AEs(bytes(proto_bytes).hex())

        host = "loginbp.ggpolarbear.com"
        register_url = Config.MAJOR_REGISTER_URL
        login_url    = Config.MAJOR_LOGIN_URL

        headers_reg = {
            "Accept-Encoding": "gzip", "Authorization": "Bearer",
            "Connection": "Keep-Alive", "Content-Type": "application/x-www-form-urlencoded",
            "Expect": "100-continue", "Host": host,
            "ReleaseVersion": "OB54",
            "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 9; ASUS_I005DA Build/PI)",
            "X-GA": "v1 1", "X-Unity-Version": "1.126.1",
        }

        resp_reg = session.post(register_url, headers=headers_reg,
                                data=encrypted_payload, verify=False, timeout=15)
        if resp_reg.status_code != 200:
            return None

        login_result = _perform_major_login_sync(uid, password, access_token, open_id,
                                                  region, session, is_ghost)
        account_id = login_result.get("account_id", "N/A")
        jwt_token  = login_result.get("jwt_token", "")
        ml_key     = login_result.get("ml_key")
        ml_iv      = login_result.get("ml_iv")
        ml_ts      = login_result.get("ml_timestamp")
        ml_url     = login_result.get("ml_url")

        if not is_ghost and jwt_token and account_id != "N/A" and region.upper() != "BR":
            _force_region_binding(region, jwt_token, session)
            _select_veteran(region, jwt_token, session)

        tcp_ok = False
        if jwt_token and account_id != "N/A":
            tcp_ok = _activate_via_tcp(
                account_id, jwt_token, ml_ts, ml_key, ml_iv,
                open_id, access_token, ml_url, session
            )

        return {
            "uid": uid, "password": password, "name": name,
            "region": "GHOST" if is_ghost else region,
            "status": "success", "account_id": account_id,
            "jwt_token": jwt_token, "api_label": api_config["label"],
            "tcp_activated": tcp_ok,
            "ml_url": ml_url,
        }
    except Exception as e:
        debug_print(f"MajorRegister error: {str(e)[:50]}")
        return None

def _encrypt_major_login_proto(open_id, access_token):
    if not NEW_PROTO_AVAILABLE or not AES_AVAILABLE:
        return None
    try:
        ml = MajoRLoGinrEq_pb2.MajorLogin()
        ml.event_time = str(datetime.now())[:-7]
        ml.game_name = "free fire"
        ml.platform_id = 2
        ml.client_version = "1.126.4"
        ml.client_version_code = "2024010012"
        ml.system_software = "Android OS 11 / API-30 (RQ3A.210805.001)"
        ml.system_hardware = "Handheld"
        ml.device_type = "Handheld"
        ml.telecom_operator = "Verizon"
        ml.network_operator_a = "Verizon"
        ml.network_type = "WIFI"
        ml.network_type_a = "WIFI"
        ml.screen_width = 1080
        ml.screen_height = 2400
        ml.screen_dpi = "440"
        ml.processor_details = "ARMv8"
        ml.cpu_type = 2
        ml.cpu_architecture = "64"
        ml.memory = 6144
        ml.gpu_renderer = "Adreno (TM) 650"
        ml.gpu_version = "OpenGL ES 3.2 V@1.50"
        ml.graphics_api = "OpenGLES3"
        ml.unique_device_id = f"Google|{os.urandom(16).hex() if hasattr(os, 'urandom') else '74b585a9-0268-4ad3-8f36-ef41d2e53610'}"
        ml.client_ip = ""
        ml.language = "en"
        ml.open_id = open_id
        ml.open_id_type = "4"
        ml.login_open_id_type = 4
        ml.access_token = access_token
        ml.login_by = 3
        ml.platform_sdk_id = 2
        ml.origin_platform_type = "4"
        ml.primary_platform_type = "4"
        ml.memory_available.version = 55
        ml.memory_available.hidden_value = 81
        ml.external_storage_total = 128512
        ml.external_storage_available = 42000
        ml.internal_storage_total = 110731
        ml.internal_storage_available = 25000
        ml.game_disk_storage_total = 26628
        ml.game_disk_storage_available = 22000
        ml.external_sdcard_total_storage = 119234
        ml.external_sdcard_avail_storage = 50000
        ml.library_path = "/data/app/~~random/base.apk"
        ml.library_token = "hash|base.apk"
        ml.client_using_version = "7428b253defc164018c604a1ebbfebdf"
        ml.supported_astc_bitset = 16383
        ml.analytics_detail = b"FwQVTgUPX1UaUllDDwcWCRBpWAUOUgsvA1snWlBaO1kFYg=="
        ml.loading_time = 13564
        ml.release_channel = "android"
        ml.channel_type = 3
        ml.reg_avatar = 1
        ml.if_push = 1
        ml.is_vpn = 0
        ml.android_engine_init_flag = 110009
        serialized = ml.SerializeToString()
        key_b = bytes([89,103,38,116,99,37,68,69,117,104,54,37,90,99,94,56])
        iv_b  = bytes([54,111,121,90,68,114,50,50,69,51,121,99,104,106,77,37])
        cipher = AES.new(key_b, AES.MODE_CBC, iv_b)
        return cipher.encrypt(pad(serialized, AES.block_size))
    except Exception as e:
        debug_print(f"Proto MajorLogin build error: {e}")
        return None

def _perform_major_login_sync(uid, password, access_token, open_id, region, session, is_ghost=False):
    url = Config.MAJOR_LOGIN_URL
    headers = {
        "Accept-Encoding": "gzip", "Authorization": "Bearer",
        "Connection": "Keep-Alive", "Content-Type": "application/x-www-form-urlencoded",
        "Expect": "100-continue", "Host": "loginbp.ggpolarbear.com",
        "ReleaseVersion": "OB54",
        "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 9; ASUS_I005DA Build/PI)",
        "X-GA": "v1 1", "X-Unity-Version": "2018.4.11f1",
    }

    final_payload = None
    if NEW_PROTO_AVAILABLE and AES_AVAILABLE:
        try:
            final_payload = _encrypt_major_login_proto(open_id, access_token)
            debug_print(f"MajorLogin (proto/new) for {uid}")
        except Exception as e:
            debug_print(f"Proto build failed, falling back: {e}")
            final_payload = None

    if final_payload is None:
        try:
            lang = "pt" if is_ghost else Config.REGION_LANG.get(region.upper(), "en")
            payload_parts = [
                b'\x1a\x132025-08-30 05:19:21\"\tfree fire(\x01:\x081.114.13B2Android OS 9 / API-28 (PI/rel.cjw.20220518.114133)J\x08HandheldR\nATM MobilsZ\x04WIFI`\xb6\nh\xee\x05r\x03300z\x1fARMv7 VFPv3 NEON VMH | 2400 | 2\x80\x01\xc9\x0f\x8a\x01\x0fAdreno (TM) 640\x92\x01\rOpenGL ES 3.2\x9a\x01+Google|dfa4ab4b-9dc4-454e-8065-e70c733fa53f\xa2\x01\x0e105.235.139.91\xaa\x01\x02',
                lang.encode("ascii"),
                b'\xb2\x01 1d8ec0240ede109973f3321b9354b44d\xba\x01\x014\xc2\x01\x08Handheld\xca\x01\x10Asus ASUS_I005DA\xea\x01@afcfbf13334be42036e4f742c80b956344bed760ac91b3aff9b607a610ab4390\xf0\x01\x01\xca\x02\nATM Mobils\xd2\x02\x04WIFI\xca\x03 7428b253defc164018c604a1ebbfebdf\xe0\x03\xa8\x81\x02\xe8\x03\xf6\xe5\x01\xf0\x03\xaf\x13\xf8\x03\x84\x07\x80\x04\xe7\xf0\x01\x88\x04\xa8\x81\x02\x90\x04\xe7\xf0\x01\x98\x04\xa8\x81\x02\xc8\x04\x01\xd2\x04=/data/app/com.dts.freefireth-PdeDnOilCSFn37p1AH_FLg==/lib/arm\xe0\x04\x01\xea\x04_2087f61c19f57f2af4e7feff0b24d9d9|/data/app/com.dts.freefireth-PdeDnOilCSFn37p1AH_FLg==/base.apk\xf0\x04\x03\xf8\x04\x01\x8a\x05\x0232\x9a\x05\n2019118693\xb2\x05\tOpenGLES2\xb8\x05\xff\x7f\xc0\x05\x04\xe0\x05\xf3F\xea\x05\x07android\xf2\x05pKqsHT5ZLWrYljNb5Vqh//yFRlaPHSO9NWSQsVvOmdhEEn7W+VHNUK+Q+fduA3ptNrGB0Ll0LRz3WW0jOwesLj6aiU7sZ40p8BfUE/FI/jzSTwRe2\xf8\x05\xfb\xe4\x06\x88\x06\x01\x90\x06\x01\x9a\x06\x014\xa2\x06\x014\xb2\x06"GQ@O\x00\x0e^\x00D\x06UA\x0ePM\r\x13hZ\x07T\x06\x0cm\\V\x0ejYV;\x0bU5'
            ]
            payload_bytes = b''.join(payload_parts)
            payload_bytes = payload_bytes.replace(
                b'afcfbf13334be42036e4f742c80b956344bed760ac91b3aff9b607a610ab4390',
                access_token.encode()
            )
            payload_bytes = payload_bytes.replace(b'1d8ec0240ede109973f3321b9354b44d', open_id.encode())
            d = encrypt_api(payload_bytes.hex())
            if d:
                final_payload = bytes.fromhex(d)
            debug_print(f"MajorLogin (legacy) for {uid}")
        except Exception as e:
            debug_print(f"Legacy payload error: {e}")
            return {"account_id": "N/A", "jwt_token": ""}

    if final_payload is None:
        return {"account_id": "N/A", "jwt_token": ""}

    try:
        response = session.post(url, headers=headers, data=final_payload, verify=False, timeout=15)
        if response.status_code == 200 and len(response.content) > 10:
            if NEW_PROTO_AVAILABLE:
                try:
                    res = MajoRLoGinrEs_pb2.MajorLoginRes()
                    res.ParseFromString(response.content)
                    if res.token:
                        account_id = str(res.account_uid) if res.account_uid else decode_jwt_token(res.token)
                        key_bytes = bytes(res.key) if res.key else None
                        iv_bytes  = bytes(res.iv)  if res.iv  else None
                        return {
                            "account_id": account_id,
                            "jwt_token":  res.token,
                            "ml_key":     key_bytes,
                            "ml_iv":      iv_bytes,
                            "ml_timestamp": str(res.timestamp) if res.timestamp else None,
                            "ml_url":     res.url if res.url else None,
                        }
                except Exception as pe:
                    debug_print(f"Proto parse error: {pe}")
                    pass
            text = response.text
            jwt_start = text.find("eyJ")
            if jwt_start != -1:
                jwt_token = text[jwt_start:]
                second_dot = jwt_token.find(".", jwt_token.find(".") + 1)
                if second_dot != -1:
                    jwt_token = jwt_token[:second_dot + 44]
                    account_id = decode_jwt_token(jwt_token)
                    return {"account_id": account_id, "jwt_token": jwt_token,
                            "ml_key": None, "ml_iv": None,
                            "ml_timestamp": None, "ml_url": None}
    except Exception as e:
        debug_print(f"MajorLogin request error: {e}")

    return {"account_id": "N/A", "jwt_token": "",
            "ml_key": None, "ml_iv": None, "ml_timestamp": None, "ml_url": None}


# =============================================================================
# 🔌 TCP ACCOUNT ACTIVATION
# =============================================================================

def _build_auth_token_hex(account_id, jwt_token, timestamp, key_bytes, iv_bytes):
    try:
        uid = int(account_id)
        uid_hex = hex(uid)[2:]
        uid_length = len(uid_hex)
        ts = int(timestamp)
        ts_hex = hex(ts)[2:]
        if len(ts_hex) == 1:
            ts_hex = "0" + ts_hex

        cipher = AES.new(key_bytes, AES.MODE_CBC, iv_bytes)
        encrypted_token = cipher.encrypt(pad(jwt_token.encode(), AES.block_size))
        encrypted_hex   = encrypted_token.hex()
        enc_len_hex     = hex(len(encrypted_hex) // 2)[2:]

        if uid_length == 9:
            headers_str = '0000000'
        elif uid_length == 8:
            headers_str = '00000000'
        elif uid_length == 10:
            headers_str = '000000'
        elif uid_length == 7:
            headers_str = '000000000'
        else:
            headers_str = '0000000'

        return f"0115{headers_str}{uid_hex}{ts_hex}00000{enc_len_hex}{encrypted_hex}"
    except Exception as e:
        debug_print(f"Auth token build error: {e}")
        return None

def _get_login_data_sync(base_url, open_id, access_token, jwt_token, session):
    try:
        if not NEW_PROTO_AVAILABLE:
            return None, None
        payload = _encrypt_major_login_proto(open_id, access_token)
        if payload is None:
            return None, None
        url = f"{base_url}/GetLoginData"
        host = base_url.replace("https://", "").replace("http://", "")
        headers = {
            "Accept-Encoding": "gzip",
            "Authorization": f"Bearer {jwt_token}",
            "Connection": "Keep-Alive",
            "Content-Type": "application/x-www-form-urlencoded",
            "Expect": "100-continue",
            "Host": host,
            "ReleaseVersion": "OB54",
            "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 9; ASUS_I005DA Build/PI)",
            "X-GA": "v1 1",
            "X-Unity-Version": "2018.4.11f1",
        }
        resp = session.post(url, headers=headers, data=payload, verify=False, timeout=15)
        if resp.status_code == 200 and resp.content:
            data = PorTs_pb2.GetLoginData()
            data.ParseFromString(resp.content)
            online_ip_port = data.Online_IP_Port if data.Online_IP_Port else None
            chat_ip_port   = data.AccountIP_Port if data.AccountIP_Port else None
            return online_ip_port, chat_ip_port
    except Exception as e:
        debug_print(f"GetLoginData error: {e}")
    return None, None

async def _tcp_connect_and_activate(ip, port, auth_hex, server_name, duration=0.8):
    try:
        reader, writer = await asyncio.open_connection(ip, int(port), ssl=False)
        debug_print(f"TCP connected to {server_name} {ip}:{port}")
        writer.write(bytes.fromhex(auth_hex))
        await writer.drain()
        debug_print(f"TCP auth sent to {server_name}")
        await asyncio.sleep(duration)
        writer.close()
        await writer.wait_closed()
        debug_print(f"TCP disconnected from {server_name}")
        return True
    except Exception as e:
        debug_print(f"TCP error {server_name} {ip}:{port} — {e}")
        return False

def _activate_via_tcp(account_id, jwt_token, timestamp, key_bytes, iv_bytes,
                      open_id, access_token, ml_url, session):
    try:
        if not (key_bytes and iv_bytes and timestamp and ml_url):
            debug_print("TCP activation skipped: missing key/iv/timestamp/url")
            return False

        online_ip_port, chat_ip_port = _get_login_data_sync(
            ml_url, open_id, access_token, jwt_token, session
        )
        if not online_ip_port and not chat_ip_port:
            debug_print("TCP activation: no server IP returned from GetLoginData")
            return False

        auth_hex = _build_auth_token_hex(account_id, jwt_token, timestamp, key_bytes, iv_bytes)
        if not auth_hex:
            return False

        debug_print(f"TCP activating account {account_id} via {online_ip_port} + {chat_ip_port}")

        async def _run():
            tasks = []
            if online_ip_port and ":" in online_ip_port:
                ip, port = online_ip_port.split(":")
                tasks.append(_tcp_connect_and_activate(ip, port, auth_hex, "Online"))
            if chat_ip_port and ":" in chat_ip_port:
                ip, port = chat_ip_port.split(":")
                tasks.append(_tcp_connect_and_activate(ip, port, auth_hex, "Chat"))
            if tasks:
                results = await asyncio.gather(*tasks, return_exceptions=True)
                return any(r is True for r in results)
            return False

        loop = asyncio.new_event_loop()
        try:
            result = loop.run_until_complete(_run())
        finally:
            loop.close()
        return result
    except Exception as e:
        debug_print(f"TCP activation error: {e}")
        return False

def _force_region_binding(region, jwt_token, session):
    try:
        url = ("https://loginbp.common.ggbluefox.com/ChooseRegion"
               if region.upper() in ["ME","TH"]
               else "https://loginbp.ggpolarbear.com/ChooseRegion")
        region_code = "RU" if region.upper() == "CIS" else region.upper()
        fields = {1: region_code}
        proto_data = run_async(CrEaTe_ProTo(fields))
        encrypted_data = encrypt_api(bytes(proto_data).hex())
        payload = bytes.fromhex(encrypted_data)
        headers = {
            'User-Agent': "Dalvik/2.1.0 (Linux; U; Android 12; M2101K7AG Build/SKQ1.210908.001)",
            'Connection': "Keep-Alive", 'Accept-Encoding': "gzip",
            'Content-Type': "application/x-www-form-urlencoded", 'Expect': "100-continue",
            'Authorization': f"Bearer {jwt_token}", 'X-Unity-Version': "1.126.1",
            'X-GA': "v1 1", 'ReleaseVersion': "OB54",
        }
        response = session.post(url, data=payload, headers=headers, verify=False, timeout=15)
        return response.status_code == 200
    except:
        return False

def _select_veteran(region, jwt_token, session):
    try:
        url = ("https://clientbp.common.ggbluefox.com/ActiveBeginnerGuide"
               if region.upper() in ["ME","TH"]
               else "https://clientbp.ggpolarbear.com/ActiveBeginnerGuide")
        fields = {1: 3}
        proto_data = run_async(CrEaTe_ProTo(fields))
        encrypted_data = encrypt_api(bytes(proto_data).hex())
        payload = bytes.fromhex(encrypted_data)
        headers = {
            'User-Agent': "Dalvik/2.1.0 (Linux; U; Android 12; M2101K7AG Build/SKQ1.210908.001)",
            'Connection': "Keep-Alive", 'Accept-Encoding': "gzip",
            'Content-Type': "application/x-www-form-urlencoded",
            'Authorization': f"Bearer {jwt_token}", 'X-Unity-Version': "2018.4.11f1",
            'X-GA': "v1 1", 'ReleaseVersion': "OB54",
        }
        response = session.post(url, data=payload, headers=headers, verify=False, timeout=15)
        return response.status_code == 200
    except:
        return False

# =============================================================================
# 🔥 AUTO ACTIVATION INTEGRATION
# =============================================================================

ACTIVATED_COUNTER      = 0
FAILED_ACTIVATION_COUNTER = 0

def auto_activate_account(account_data):
    global ACTIVATED_COUNTER, FAILED_ACTIVATION_COUNTER
    if not Config.AUTO_ACT:
        return False
    try:
        activator = AutoActivator(max_workers=1, turbo_mode=True)
        success = activator.activate_account(account_data)
        with Config.LOCK:
            if success:
                ACTIVATED_COUNTER += 1
                save_activated_account(account_data)
                account_data['tcp_activated'] = True
            else:
                FAILED_ACTIVATION_COUNTER += 1
                save_failed_activation(account_data)
        return success
    except Exception as e:
        with Config.LOCK:
            FAILED_ACTIVATION_COUNTER += 1
        return False

# =============================================================================
# 🔌 GARENA EMOTE EQUIP INTEGRATION MODULE (FROM 1.py)
# =============================================================================

def decode_jwt_payload(token):
    try:
        parts = token.split('.')
        if len(parts) != 3:
            return None
        payload_b64 = parts[1]
        payload_b64 += '=' * ((4 - len(payload_b64) % 4) % 4)
        payload_bytes = base64.urlsafe_b64decode(payload_b64)
        return json.loads(payload_bytes)
    except Exception:
        return None

def get_region_from_payload(payload):
    return payload.get("noti_region") or payload.get("lock_region")

def equip_emote(jwt_token, session):
    """Sends ChooseEmote request using base64/hex protocols and raw body payload"""
    if not jwt_token:
        return "FAILED (NO JWT)"
    
    payload = decode_jwt_payload(jwt_token)
    if not payload:
        return "FAILED (INVALID JWT)"
    
    region = get_region_from_payload(payload)
    if not region:
        return "FAILED (NO REGION)"
        
    server_url = REGION_SERVER_MAP.get(region.upper())
    if not server_url:
        return f"FAILED (NO SERVER FOR {region})"
        
    url = f"{server_url}/ChooseEmote"
    headers = {
        "Accept-Encoding": "gzip",
        "Connection": "Keep-Alive",
        "Content-Type": "application/x-www-form-urlencoded",
        "Expect": "100-continue",
        "ReleaseVersion": "OB54",
        "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 11; SM-A515F Build/RP1A.200720.012)",
        "X-GA": "v1 1",
        "X-Unity-Version": "2018.4.11f1",
        "Authorization": f"Bearer {jwt_token}"
    }
    
    try:
        emote_data = bytes.fromhex("CAF683222A25C7BEFEB51F59544DB313")
        resp = session.post(url, headers=headers, data=emote_data, verify=False, timeout=12)
        if resp.status_code == 200:
            preview = resp.text
            if "BR_INVENTORY_NOT_ENOUGH_ITEMS" in preview:
                return "FAILED (NOT IN INVENTORY)"
            return "SUCCESS"
        else:
            return f"FAILED ({resp.status_code})"
    except Exception as e:
        return f"FAILED (ERR: {str(e)[:15]})"

# =============================================================================
# 🔌 SYNCHRONOUS GARENA FRIEND REQUEST SENDER MODULE
# =============================================================================

def send_friend_request(session, author_uid, target_uid, jwt_token, base_url):
    """Encodes and fires a secure RequestAddingFriend protobuf payload over Garena session"""
    try:
        payload_fields = {
            1: int(author_uid),
            2: int(target_uid),
            3: 1
        }
        proto_data = run_async(CrEaTe_ProTo(payload_fields))
        encrypted = E_AEs(bytes(proto_data).hex())

        headers = {
            "Authorization": f"Bearer {jwt_token}",
            "X-Unity-Version": "2018.4.11f1",
            "X-GA": "v1 1",
            "ReleaseVersion": "OB54",
            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": "Dalvik/2.1.0 (Linux; Android 9)"
        }
        url = f"{base_url}/RequestAddingFriend"

        for attempt in range(1, 4):
            try:
                resp = session.post(url, headers=headers, data=encrypted, verify=False, timeout=10)
                if resp.status_code == 200:
                    return "SUCCESS"
                if resp.status_code == 401:
                    return "UNAUTHORIZED"
            except:
                pass
            time.sleep(0.1)
    except Exception as e:
        debug_print(f"Garena Friend Request Sender Error: {e}")
    return "FAILED"

# =============================================================================
# 🛡️ SYNCHRONOUS GARENA CLAN/GUILD JOIN REQUEST SENDER MODULE (LIMIT: 40)
# =============================================================================

def send_clan_join_request(session, author_uid, clan_id, jwt_token, base_url):
    """Encodes and fires a RequestJoinClan protobuf payload over Garena session (OB54 Support)"""
    try:
        message = reqClan_pb2.MyMessage()
        message.field_1 = int(clan_id)
        serialized_data = message.SerializeToString()
        encrypted = E_AEs(serialized_data)

        headers = {
            "Authorization": f"Bearer {jwt_token}",
            "X-Unity-Version": "2018.4.11f1",
            "X-GA": "v1 1",
            "ReleaseVersion": "OB54",
            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": "Dalvik/2.1.0 (Linux; Android 9)"
        }
        url = f"{base_url}/RequestJoinClan"

        for attempt in range(1, 11):
            try:
                resp = session.post(url, headers=headers, data=encrypted, verify=False, timeout=10)
                if resp.status_code == 200:
                    return "SUCCESS"
                if resp.status_code == 401:
                    return "UNAUTHORIZED"
                if resp.status_code == 403:
                    return "FORBIDDEN"
            except:
                pass
            time.sleep(0.1)
    except Exception as e:
        debug_print(f"Garena Guild Join Request Sender Error: {e}")
    return "FAILED"

# =============================================================================
# 💾 SAVE FUNCTIONS
# =============================================================================

def save_ariyan_txt(uid, password):
    """Appends account details in flat text format strictly inside current Accounts Folder"""
    try:
        filepath = os.path.join(Config.ACCOUNTS_FOLDER, "ariyan.txt")
        with get_file_lock(filepath):
            with open(filepath, "a", encoding="utf-8") as f:
                f.write(f"{uid}:{password}\n")
    except Exception as e:
        debug_print(f"Failed to append to ariyan.txt: {e}")

def save_activated_account(account_data):
    try:
        activated_name = getattr(Config, 'CURRENT_ACTIVATED_BASE', 'activated')
        filename = os.path.join(Config.ACTIVATED_FOLDER, f"{activated_name}.json")
        entry = {
            'uid': account_data['uid'], 'password': account_data['password'],
            'account_id': account_data.get('account_id','N/A'),
            'name': account_data['name'], 'region': account_data.get('region','UNKNOWN'),
            'activated_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        with get_file_lock(filename):
            lst = safe_json_load(filename, [])
            lst.append(entry)
            safe_json_save(filename, lst)
    except: pass

def save_failed_activation(account_data):
    try:
        region = account_data.get('region', 'UNKNOWN')
        filename = os.path.join(Config.FAILED_ACTIVATION_FOLDER, f"failed-{region}.json")
        entry = {
            'uid': account_data['uid'], 'password': account_data['password'],
            'account_id': account_data.get('account_id','N/A'),
            'name': account_data['name'], 'region': region,
            'failed_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        with get_file_lock(filename):
            lst = safe_json_load(filename, [])
            lst.append(entry)
            safe_json_save(filename, lst)
    except: pass

def save_jwt_token(account_data, jwt_token, region, is_ghost=False):
    try:
        filename = (os.path.join(Config.GHOST_FOLDER, "tokens-ghost.json") if is_ghost
                    else os.path.join(Config.TOKENS_FOLDER, f"tokens-{region}.json"))
        entry = {
            'uid': account_data["uid"], 'account_id': account_data.get("account_id","N/A"),
            'jwt_token': jwt_token, 'name': account_data["name"],
            'password': account_data["password"],
            'date_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'region': "ARIYAN" if is_ghost else region,
            'thread_id': account_data.get('thread_id','N/A')
        }
        with get_file_lock(filename):
            lst = safe_json_load(filename, [])
            existing = [t.get('account_id') for t in lst]
            if account_data.get("account_id","N/A") not in existing:
                lst.append(entry)
                safe_json_save(filename, lst)
                return True
        return False
    except: return False

def save_normal_account(account_data, region, is_ghost=False):
    try:
        if is_ghost:
            filename = os.path.join(Config.GHOST_ACCOUNTS_FOLDER, "ghost.json")
        else:
            json_base = getattr(Config, 'CURRENT_JSON_BASE', f'accounts-{region}')
            filename = os.path.join(Config.ACCOUNTS_FOLDER, f"{json_base}.json")
        entry = {
            'uid': account_data["uid"], 'password': account_data["password"],
            'account_id': account_data.get("account_id","N/A"), 'name': account_data["name"],
            'region': "ARIYAN" if is_ghost else region,
            'date_created': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'thread_id': account_data.get('thread_id','N/A')
        }
        with get_file_lock(filename):
            lst = safe_json_load(filename, [])
            existing = [a.get('account_id') for a in lst]
            if account_data.get("account_id","N/A") not in existing:
                lst.append(entry)
                safe_json_save(filename, lst)
                return True
        return False
    except: return False

def save_rare_account(account_data, rarity_type, reason, rarity_score, is_ghost=False):
    if rarity_score < 10:
        debug_print(f"Rare score {rarity_score} < 10 — not saved to file")
        return False
    try:
        filename = (os.path.join(Config.GHOST_RARE_FOLDER, "rare-ghost.json") if is_ghost
                    else os.path.join(Config.RARE_ACCOUNTS_FOLDER, f"rare-{account_data.get('region','UNKNOWN')}.json"))
        entry = {
            'uid': account_data["uid"], 'password': account_data["password"],
            'account_id': account_data.get("account_id","N/A"), 'name': account_data["name"],
            'region': "ARIYAN" if is_ghost else account_data.get('region','UNKNOWN'),
            'rarity_type': rarity_type, 'rarity_score': rarity_score, 'reason': reason,
            'date_identified': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'jwt_token': account_data.get('jwt_token',''), 'thread_id': account_data.get('thread_id','N/A')
        }
        with get_file_lock(filename):
            lst = safe_json_load(filename, [])
            existing = [a.get('account_id') for a in lst]
            if account_data.get("account_id","N/A") not in existing:
                lst.append(entry)
                safe_json_save(filename, lst)
                return True
        return False
    except: return False

def save_couples_account(account1, account2, reason, is_ghost=False):
    try:
        region = account1.get('region','UNKNOWN')
        filename = (os.path.join(Config.GHOST_COUPLES_FOLDER, "couples-ghost.json") if is_ghost
                    else os.path.join(Config.COUPLES_ACCOUNTS_FOLDER, f"couples-{region}.json"))
        entry = {
            'couple_id': f"{account1.get('account_id','N/A')}_{account2.get('account_id','N/A')}",
            'account1': {'uid': account1["uid"], 'password': account1["password"],
                         'account_id': account1.get("account_id","N/A"), 'name': account1["name"],
                         'thread_id': account1.get('thread_id','N/A')},
            'account2': {'uid': account2["uid"], 'password': account2["password"],
                         'account_id': account2.get("account_id","N/A"), 'name': account2["name"],
                         'thread_id': account2.get('thread_id','N/A')},
            'reason': reason, 'region': "ARIYAN" if is_ghost else region,
            'date_matched': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        with get_file_lock(filename):
            lst = safe_json_load(filename, [])
            existing = [c.get('couple_id') for c in lst]
            if entry['couple_id'] not in existing:
                lst.append(entry)
                safe_json_save(filename, lst)
                return True
        return False
    except: return False

# =============================================================================
# 👥 WORKER FUNCTIONS (CYBER-GRADIENT OUTPUT INTERFACE)
# =============================================================================

RARE_COUNTER    = 0
COUPLES_COUNTER = 0
SUCCESS_COUNTER = 0

def print_registration_status(count, total, name, uid, password, account_id, region, is_ghost=False, api_label="OB54", jwt_token="", activated_state="N/A", bio_state="N/A", applied_bio="", freq_state="N/A", clan_state="N/A", emote_state="N/A"):
    C   = VISUAL.COLORS
    R   = C['reset']; B = C['bold']
    W   = 60

    color_keys = ['c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'primary', 'secondary', 'success', 'warning', 'rare', 'couple', 'info']
    selected_color_key = color_keys[(count - 1) % len(color_keys)]
    
    border_col  = C[selected_color_key]
    hdr_txt_col = C['accent']
    key_col     = C['accent']
    val_col     = C['success']

    INNER = W - 4

    def box_line(text_colored, text_plain):
        pad = max(0, INNER - len(text_plain))
        print(f"{border_col}║{R} {text_colored}{' '*pad} {border_col}║{R}")

    def row(icon, key, val, vc=val_col):
        label     = f"{icon} {key:<16}"
        label_len = len(label)
        val_s     = str(val)
        avail     = INNER - label_len

        if len(val_s) <= avail:
            plain = label + val_s
            colored = f"{key_col}{B}{label}{R}{vc}{val_s}{R}"
            box_line(colored, plain)
        else:
            chunk1 = val_s[:avail]
            plain1 = label + chunk1
            colored1 = f"{key_col}{B}{label}{R}{vc}{chunk1}{R}"
            box_line(colored1, plain1)
            indent = " " * (label_len)
            rest   = val_s[avail:]
            avail2 = INNER - label_len
            while rest:
                chunk = rest[:avail2]
                rest  = rest[avail2:]
                padding2 = avail2 - len(chunk)
                plain2   = indent + chunk
                colored2 = f"{vc}{indent}{chunk}{R}"
                box_line(colored2, plain2)

    hdr_txt  = f"✨ ARIYAN SYSTEM: SUCCESSFUL REGISTRATION! [{count}/{total}]"
    hdr_plain= f"   ARIYAN SYSTEM: SUCCESSFUL REGISTRATION! [{count}/{total}]"
    print(f"{border_col}╔{'═' * (W-2)}╗{R}")
    hdr_pad  = max(0, INNER - len(hdr_plain))
    print(f"{border_col}║{R} {hdr_txt_col}{B}{hdr_txt}{R}{' '*hdr_pad} {border_col}║{R}")
    print(f"{border_col}╠{'═' * (W-2)}╣{R}")

    row("🆔", "UID Code:",        str(uid), C['success'])
    pwd_visible = 8
    pwd_avail = INNER - 20
    pwd_stars = max(0, pwd_avail - pwd_visible)
    pwd_display = str(password)[:pwd_visible] + ("*" * pwd_stars)
    row("🔑", "Passkey:",         pwd_display, C['warning'])
    row("👤", "Name Tag:",        str(name), C['accent'])
    row("🎮", "Account ID:",      str(account_id), C['primary'])
    row("⚡", "Activation:",      str(activated_state), C['secondary'])
    row("📝", "Bio Status:",      str(bio_state), C['couple'])

    if bio_state == "SUCCESSFULLY APPLIED" and applied_bio:
        if "\n" in applied_bio:
            lines = applied_bio.split('\n')
            for index, line in enumerate(lines, 1):
                term_colored_line = garena_bio_to_terminal(line)
                raw_line = re.sub(r'\[[0-9A-Fa-f]{6}\]', '', line)
                label = f"🧬 Font Row {index}:"
                space_left = INNER - len(label)
                if len(raw_line) <= space_left:
                    padding = space_left - len(raw_line)
                    print(f"{border_col}║ {key_col}{B}{label:<16}{R}{term_colored_line}{' ' * padding} {border_col}║{R}")
                else:
                    print(f"{border_col}║ {key_col}{B}{label:<16}{R}{term_colored_line[:space_left]} {border_col}║{R}")
        else:
            row("🧬", "Bio Signature:",   str(applied_bio), C['highlight'])

    if Config.SEND_FRIEND_REQ:
        row("🔌", "Friend Request:",  str(freq_state), C['success'] if freq_state == "SENT" else C['error'])

    if Config.SEND_CLAN_REQ:
        row("🛡️", "Guild Join:",      str(clan_state), C['success'] if clan_state == "SENT" else C['error'])

    # Display Emote Equip Status cleanly in terminal output
    if Config.AUTO_EMOTE:
        row("🎭", "Emote Equip:",     str(emote_state), C['success'] if emote_state == "SUCCESS" else C['error'])

    ts_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    row("⏱️", "Timestamp:",       ts_now, C['info'])

    jwt_visible = 10
    jwt_stars = max(0, pwd_avail - jwt_visible)
    jwt_display = jwt_token[:jwt_visible] + ("*" * jwt_stars) if jwt_token else "N/A"
    row("🔒", "JWT Token:",       jwt_display, C['dim'])

    print(f"{border_col}╚{'═' * (W-2)}╝{R}")
    print()

def generate_single_account(region, total_accounts, thread_id, session, is_ghost=False):
    global SUCCESS_COUNTER, RARE_COUNTER, COUPLES_COUNTER, BIO_SET_COUNTER
    global ACTIVATED_COUNTER, FAILED_ACTIVATION_COUNTER

    if EXIT_FLAG:
        return None

    with Config.LOCK:
        if SUCCESS_COUNTER >= total_accounts:
            return None

    account_result = create_acc(region, session, is_ghost)
    if not account_result:
        return None

    account_id = account_result.get("account_id", "N/A")
    jwt_token  = account_result.get("jwt_token", "")
    api_label  = account_result.get("api_label", "OB54")
    ml_url     = account_result.get("ml_url")
    account_result['thread_id'] = thread_id

    tcp_ok = account_result.get("tcp_activated", False)
    activated_state = "ACTIVATION INACTIVE"

    if is_ghost:
        save_normal_account(account_result, "GHOST", is_ghost=True)
        save_ariyan_txt(account_result["uid"], account_result["password"])
        if jwt_token: save_jwt_token(account_result, jwt_token, "GHOST", is_ghost=True)
    else:
        save_normal_account(account_result, region)
        save_ariyan_txt(account_result["uid"], account_result["password"])
        if jwt_token: save_jwt_token(account_result, jwt_token, region)

        # 1. Activation Step
        if tcp_ok:
            with Config.LOCK:
                ACTIVATED_COUNTER += 1
            save_activated_account(account_result)
            activated_state = "ACTIVATED (TCP)"
        elif Config.AUTO_ACT:
            act_success = auto_activate_account(account_result)
            if act_success:
                activated_state = "ACTIVATED (AUTO HTTP)"
            else:
                activated_state = "ACTIVATION FAILED"
        else:
            activated_state = "ACTIVATION SKIPPED"

    # 2. Bio Step
    bio_state = "DISABLED"
    applied_bio = ""
    if Config.AUTO_BIO:
        if getattr(Config, 'BIO_MODE', 'Y') == "MX":
            name_to_use = getattr(Config, 'MX_NAME', 'ARIYAN')[:6]
            color_choices = [random.choice(BIO_COLORS) for _ in range(len(name_to_use))]
            l1, l2, l3 = "", "", ""
            for idx, char in enumerate(name_to_use):
                font_lines = BLOCK_FONT.get(char, BLOCK_FONT[' '])
                color_code = f"[{color_choices[idx]}]"
                l1 += f"[b][c]{color_code}{font_lines[0]}"
                l2 += f"{color_code}{font_lines[1]}"
                l3 += f"{font_lines[2]}"
            bio_signature = f"{l1}\n{l2}\n{l3}"
        else:
            bio_signature = Config.BIO_TEXT

        bio_success = set_account_bio(account_result["uid"], account_result["password"],
                        bio_signature, region,
                        existing_jwt=account_result.get("jwt_token", ""),
                        base_url=ml_url)
        if bio_success:
            bio_state = "SUCCESSFULLY APPLIED"
            applied_bio = bio_signature
        else:
            bio_state = "APPLICATION FAILED"

    # 3. Friend Request Step
    freq_state = "INACTIVE"
    if Config.SEND_FRIEND_REQ and jwt_token and account_id != "N/A" and ml_url:
        try:
            author_uid = int(account_id)
            req_status = send_friend_request(session, author_uid, Config.TARGET_UID, jwt_token, ml_url)
            if req_status == "SUCCESS":
                freq_state = "SENT"
                with Config.LOCK:
                    Config.FRIEND_REQ_SUCCESS_COUNT += 1
            else:
                freq_state = f"FAILED ({req_status})"
                with Config.LOCK:
                    Config.FRIEND_REQ_FAILED_COUNT += 1
        except Exception as fe:
            freq_state = f"ERROR ({str(fe)[:10]})"
            with Config.LOCK:
                Config.FRIEND_REQ_FAILED_COUNT += 1

    # 4. Guild/Clan Join Step
    clan_state = "INACTIVE"
    if Config.SEND_CLAN_REQ and jwt_token and account_id != "N/A" and ml_url:
        with Config.LOCK:
            current_clan_success_count = Config.CLAN_REQ_SUCCESS_COUNT
        
        if current_clan_success_count >= 40:
            clan_state = "SKIPPED (LIMIT 40)"
        else:
            try:
                author_uid = int(account_id)
                clan_status = send_clan_join_request(session, author_uid, Config.TARGET_CLAN_ID, jwt_token, ml_url)
                if clan_status == "SUCCESS":
                    clan_state = "SENT"
                    with Config.LOCK:
                        Config.CLAN_REQ_SUCCESS_COUNT += 1
                elif clan_status == "FORBIDDEN":
                    clan_state = "PENDING/ALREADY"
                    with Config.LOCK:
                        Config.CLAN_REQ_FAILED_COUNT += 1
                else:
                    clan_state = f"FAILED ({clan_status})"
                    with Config.LOCK:
                        Config.CLAN_REQ_FAILED_COUNT += 1
            except Exception as ce:
                clan_state = f"ERROR ({str(ce)[:10]})"
                with Config.LOCK:
                    Config.CLAN_REQ_FAILED_COUNT += 1

    # 5. Emote Equip Step (Runs absolute last)
    emote_state = "INACTIVE"
    if Config.AUTO_EMOTE and jwt_token:
        emote_state = equip_emote(jwt_token, session)

    is_rare, rarity_type, rarity_reason, rarity_score = check_account_rarity(account_result)
    if is_rare:
        with Config.LOCK: RARE_COUNTER += 1
        save_rare_account(account_result, rarity_type, rarity_reason, rarity_score, is_ghost)

    is_couple, couple_reason, partner_data = check_account_couples(account_result, thread_id)
    if is_couple and partner_data:
        with Config.LOCK: COUPLES_COUNTER += 1
        save_couples_account(account_result, partner_data, couple_reason, is_ghost)

    VisualMaster.animate_hand_scan()

    with Config.LOCK:
        SUCCESS_COUNTER += 1
        current_count = SUCCESS_COUNTER

    print_registration_status(current_count, total_accounts, account_result["name"],
                              account_result["uid"], account_result["password"],
                              account_id, region, is_ghost, api_label,
                              jwt_token=account_result.get("jwt_token", ""),
                              activated_state=activated_state,
                              bio_state=bio_state,
                              applied_bio=applied_bio,
                              freq_state=freq_state,
                              clan_state=clan_state,
                              emote_state=emote_state)

    return {"account": account_result}

def worker(region, total_accounts, thread_id, is_ghost=False):
    session = requests.Session()
    adapter = requests.adapters.HTTPAdapter(
        pool_connections=1, pool_maxsize=4,
        max_retries=0
    )
    session.mount("https://", adapter)
    session.mount("http://", adapter)

    accounts_generated = 0
    while not EXIT_FLAG:
        with Config.LOCK:
            if SUCCESS_COUNTER >= total_accounts:
                break
        result = generate_single_account(region, total_accounts, thread_id, session, is_ghost)
        if result:
            accounts_generated += 1
    pass

# =============================================================================
# 📋 MENU FUNCTIONS
# =============================================================================

def create_menu_box(number, icon, text, color="primary"):
    colors = {
        'red': VISUAL.COLORS['error'],
        'green': VISUAL.COLORS['success'],
        'blue': VISUAL.COLORS['primary'],
        'yellow': VISUAL.COLORS['warning'],
        'purple': VISUAL.COLORS['rare'],
        'cyan': VISUAL.COLORS['secondary']
    }
    color_code = colors.get(color, VISUAL.COLORS['primary'])
    reset = VISUAL.COLORS['reset']
    bold = VISUAL.COLORS['bold']
    width = 50
    option_text = f"[{number}] {icon} {text}"
    box = f"""{color_code}┌{'─' * (width - 2)}┐{reset}
{color_code}│{reset} {bold}{color_code}{option_text.ljust(width - 4)}{reset} {color_code}│{reset}
{color_code}└{'─' * (width - 2)}┘{reset}"""
    return box

def create_region_box(number, text, color="primary"):
    colors = {
        'red': VISUAL.COLORS['error'],
        'green': VISUAL.COLORS['success'],
        'blue': VISUAL.COLORS['primary'],
        'yellow': VISUAL.COLORS['warning'],
        'purple': VISUAL.COLORS['rare'],
        'cyan': VISUAL.COLORS['secondary'],
        'pink': VISUAL.COLORS['c1'],
        'orange': VISUAL.COLORS['c6']
    }
    color_code = colors.get(color, VISUAL.COLORS['primary'])
    reset = VISUAL.COLORS['reset']
    bold = VISUAL.COLORS['bold']
    width = 54
    option_text = f"[{number}] {text}"
    box = f"""{color_code}┌{'─' * (width - 2)}┐{reset}
{color_code}│{reset} {bold}{color_code}{option_text.ljust(width - 4)}{reset} {color_code}│{reset}
{color_code}└{'─' * (width - 2)}┘{reset}"""
    return box

def generate_accounts_flow():
    global SUCCESS_COUNTER, RARE_COUNTER, COUPLES_COUNTER
    global ACTIVATED_COUNTER, FAILED_ACTIVATION_COUNTER, BIO_SET_COUNTER

    VISUAL.show_header(Config.USER_LEVEL)
    C = VISUAL.COLORS

    pass_prefix = VISUAL.get_input("PASSWORD CONFIGURATION", "꯭ᷝ✮͢𓆩𝐄𝐍𝐓𝐄𝐑 𝐏𝐀𝐒𝐒 𝐏𝐑𝐄𝐅𝐈𝐗𓆪-:)", "primary")
    if pass_prefix:
        Config.CUSTOM_PASS_PREFIX = pass_prefix

    while True:
        count_input = VISUAL.get_input("TARGET ACCOUNTS QUANTITY", "꯭✮͢𓆩𝐄𝐍𝐓𝐄𝐑 𝐀𝐂𝐂𝐎𝐔𝐍𝐓 𝐐𝐓𝐘 (𝐌𝐀𝐗 𝟗𝟗𝟗𝟗)𓆪-:)💙", "secondary")
        if count_input.isdigit():
            account_count = int(count_input)
            if account_count > 0:
                break
            else:
                print_error("Target value must be at least 1.")
        else:
            print_error("Please enter numeric digits only.")

    custom_name = VISUAL.get_input("DESIGNER USERNAME TAG", "✮͢𓆩𝐄𝐍𝐓𝐄𝐑 𝐘𝐎𝐔𝐑 𝐔𝐒𝐄𝐑𝐍𝐀𝐌𝐄 𝐎𝐑 𝐈𝐃𓆪-:)🤍", "primary")
    if custom_name:
        Config.CUSTOM_NAME_PREFIX = custom_name

    bio_choice = VISUAL.get_input("AUTO BIO CONFIGURATION", "⃪꯭̽ᷝ✮͢𓆩𝐀𝐔𝐓𝐎 𝐁𝐈𝐎 𝐌𝐎𝐃𝐄 (𝐘/𝐍/𝐌𝐗)𓆪-:)💙", "secondary").strip().upper()
    if bio_choice == 'Y':
        Config.AUTO_BIO = True
        Config.BIO_MODE = "Y"
        custom_bio = VISUAL.get_input("SOCIAL BIO PACKET", "Input your custom social Bio signature:", "primary")
        if custom_bio:
            Config.BIO_TEXT = custom_bio
    elif bio_choice == 'MX':
        Config.AUTO_BIO = True
        Config.BIO_MODE = "MX"
        mx_name = VISUAL.get_input("MAX FONT NAME INPUT", "꯭ᷝ✮͢𓆩𝐄𝐍𝐓𝐄𝐑 𝐖𝐎𝐑𝐃 (𝟔 𝐌𝐀𝐗)𓆪-:)🤍", "primary").strip().upper()
        mx_name = "".join(c for c in mx_name if c in BLOCK_FONT)[:6]
        if not mx_name:
            mx_name = "ARIYAN"
        Config.MX_NAME = mx_name
        print_success(f"Max Font Mode active for word: '{mx_name}' (Strictly 200-char limit compliant)")
    else:
        Config.AUTO_BIO = False
        Config.BIO_MODE = "N"
        print_warning("Auto Bio modification has been bypassed/disabled.")

    friend_choice = VISUAL.get_input("FRIEND SENDER MODULE", "⃪꯭̽ᷝ✮͢𓆩𝐀𝐔𝐓𝐎 𝐅𝐑𝐈𝐄𝐍𝐃 𝐑𝐄𝐐? (𝐘/𝐍)𓆪-:)🤍", "secondary").strip().upper()
    if friend_choice == 'Y':
        Config.SEND_FRIEND_REQ = True
        while True:
            target_uid_input = VISUAL.get_input("TARGET PLAYER UID", "꯭✮͢𓆩𝐄𝐍𝐓𝐄𝐑 𝐓𝐀𝐑𝐆𝐄𝐓 𝐔𝐈𝐃𓆪-:)💙", "primary")
            if target_uid_input.isdigit() and int(target_uid_input) > 0:
                Config.TARGET_UID = int(target_uid_input)
                print_success(f"Friend requests locked onto target Player UID: {Config.TARGET_UID}")
                break
            else:
                print_error("Invalid Target UID! Must be a positive integer.")
    else:
        Config.SEND_FRIEND_REQ = False
        print_warning("Friend Sender module has been bypassed/disabled.")

    # ── Guild Join module configuration ──
    clan_choice = VISUAL.get_input("GUILD JOIN MODULE", "⃪꯭̽ᷝ✮͢𓆩𝐀𝐔𝐓𝐎 𝐆𝐔𝐈𝐋𝐃 𝐉𝐎𝐈𝐍? (𝐘/𝐍)𓆪-:)🤍", "secondary").strip().upper()
    if clan_choice == 'Y':
        Config.SEND_CLAN_REQ = True
        while True:
            target_clan_input = VISUAL.get_input("TARGET GUILD ID", "꯭✮͢𓆩𝐄𝐍𝐓𝐄𝐑 𝐓𝐀𝐑𝐆𝐄𝐓 𝐆𝐔𝐈𝐋𝐃 𝐈𝐃𓆪-:)💙", "primary")
            if target_clan_input.isdigit() and int(target_clan_input) > 0:
                Config.TARGET_CLAN_ID = int(target_clan_input)
                print_success(f"Guild join requests locked onto Target Guild ID: {Config.TARGET_CLAN_ID}")
                break
            else:
                print_error("Invalid Guild ID! Must be a positive integer.")
    else:
        Config.SEND_CLAN_REQ = False
        print_warning("Guild Join module has been bypassed/disabled.")

    # ── Auto Emote Equip configuration (Interactive Y/N System) ──
    emote_choice = VISUAL.get_input("EMOTE CONFIGURATION", "⃪꯭̽ᷝ✮͢𓆩𝐀𝐔𝐓𝐎 𝐄𝐌𝐎𝐓𝐄 𝐄𝐐𝐔𝐈𝐏? (𝐘/𝐍)𓆪-:)🤍", "primary").strip().upper()
    if emote_choice == 'Y':
        Config.AUTO_EMOTE = True
        print_success("Auto Emote equipping module has been activated.")
    else:
        Config.AUTO_EMOTE = False
        print_warning("Auto Emote equipping module has been bypassed/disabled.")

    json_base_name = VISUAL.get_input("OUTPUT DATA REGISTRY", "꯭✮͢𓆩𝐎𝐔𝐓𝐏𝐔𝐓 𝐅𝐈𝐋𝐄 𝐍𝐀𝐌𝐄𓆪-:)🤍", "secondary")
    if not json_base_name:
        json_base_name = "ariyan"

    regions_to_show = [r for r in Config.REGION_LANG.keys() if r != "BR"]
    region_colors = ['green', 'blue', 'yellow', 'purple', 'cyan', 'pink', 'orange', 'green', 'blue', 'yellow']
    
    region_boxes = []
    for i, region in enumerate(regions_to_show, 1):
        full_country_name = VisualMaster.REGION_FULL_NAMES.get(region, region)
        text = f"{full_country_name:<36} (Lang: {Config.REGION_LANG[region]})"
        color = region_colors[(i - 1) % len(region_colors)]
        box = create_region_box(str(i), text, color)
        region_boxes.append(box)
    
    ghost_box = create_region_box(str(len(regions_to_show) + 1), "GHOST MODE (Zero trace BR registration)", "red")
    region_boxes.append(ghost_box)
    
    back_box = create_region_box("00", "BACK TO CORE MENU", "cyan")
    region_boxes.append(back_box)
    terminate_box = create_region_box("000", "TERMINATE SESSION", "red")
    region_boxes.append(terminate_box)
    
    region_menu = '\n'.join(region_boxes)

    print(VISUAL.create_panel("🌍 SEED GATEWAY GEOLOCATION", region_menu, color="secondary"))

    while True:
        try:
            choice = VISUAL.get_input("GATEWAY PATHWAY SELECT", "Select the gateway index from the choices above:", "secondary")
            if choice == "00": return
            elif choice == "000":
                print(f"\n{C['primary']}{C['bold']}👋 System shutdown initiated. Goodbye!{C['reset']}")
                sys.exit(0)
            elif choice.isdigit():
                n = int(choice)
                if 1 <= n <= len(regions_to_show):
                    selected_region = regions_to_show[n - 1]; is_ghost = False; break
                elif n == len(regions_to_show) + 1:
                    selected_region = "BR"; is_ghost = True; break
            elif choice in regions_to_show:
                selected_region = choice; is_ghost = False; break
            elif choice == "GHOST":
                selected_region = "BR"; is_ghost = True; break
            else:
                print_error("Invalid index option. Try again.")
        except KeyboardInterrupt:
            safe_exit()

    VISUAL.show_header(Config.USER_LEVEL)
    thread_count  = Config.MAX_THREADS

    region_suffix = selected_region.lower()
    Config.CURRENT_JSON_BASE = f"{json_base_name}-{region_suffix}"
    Config.CURRENT_ACTIVATED_BASE = f"{json_base_name}-{region_suffix}-activated"

    user_level_display = f"{'👑' if Config.USER_LEVEL=='OWNER' else '⚡' if Config.USER_LEVEL=='ADMIN' else '👤'} {Config.USER_LEVEL}"
    custom_settings = f"\n ✏️ {C['warning']}{C['bold']}Name Tag{C['reset']}    : {C['success']}{Config.CUSTOM_NAME_PREFIX}{C['reset']}\n 🔐 {C['warning']}{C['bold']}Pass Prefix{C['reset']} : {C['success']}{Config.CUSTOM_PASS_PREFIX}{C['reset']}\n ⭐ {C['warning']}{C['bold']}Rare Limit{C['reset']}  : {C['success']}{Config.CUSTOM_RARITY_THRESHOLD}{C['reset']}" if Config.USER_LEVEL in ["ADMIN","OWNER"] else ""

    region_display_name = VisualMaster.REGION_FULL_NAMES.get(selected_region.upper(), selected_region)

    config_text = f""" 🎯 {C['warning']}{C['bold']}Target Count{C['reset']}: {C['success']}{account_count}{C['reset']}
 🧵 {C['warning']}{C['bold']}Active Thread{C['reset']}: {C['success']}{thread_count}{C['reset']}
 🔌 {C['warning']}{C['bold']}Loaded APIs{C['reset']}  : {C['success']}{API_COUNT}{C['reset']}
 📝 {C['warning']}{C['bold']}Auto Bio Mod{C['reset']} : {C['success']}{'ON ('+Config.BIO_MODE+')' if Config.AUTO_BIO else 'OFF'}{C['reset']}
 ⚡ {C['warning']}{C['bold']}Friend Send{C['reset']}  : {C['success']}{'ON (Target: '+str(Config.TARGET_UID)+')' if Config.SEND_FRIEND_REQ else 'OFF'}{C['reset']}
 🛡️ {C['warning']}{C['bold']}Guild Join {C['reset']} : {C['success']}{'ON (Target: '+str(Config.TARGET_CLAN_ID)+')' if Config.SEND_CLAN_REQ else 'OFF'}{C['reset']}
 🎭 {C['warning']}{C['bold']}Auto Emote {C['reset']} : {C['success']}{'ON' if Config.AUTO_EMOTE else 'OFF'}{C['reset']}
 🔥 {C['warning']}{C['bold']}Activation{C['reset']}   : {C['success']}{'ON' if Config.AUTO_ACT else 'OFF'}{C['reset']}
 🌍 {C['warning']}{C['bold']}Region Code{C['reset']}  : {C['success']}{region_display_name}{C['reset']}
 👤 {C['warning']}{C['bold']}User Class{C['reset']}  : {C['success']}{user_level_display}{C['reset']}
 🔄 {C['warning']}{C['bold']}Retry Max{C['reset']}   : {C['success']}{Config.MAX_RETRIES}{C['reset']}
 🆕 {C['warning']}{C['bold']}Build Engine{C['reset']} : {C['success']}OB54 — RESTORED CHANNELS{C['reset']}
 👤 {C['warning']}{C['bold']}Base Username{C['reset']}: {C['success']}{Config.CUSTOM_NAME_PREFIX}{C['reset']}
 💾 {C['warning']}{C['bold']}Accounts File{C['reset']}: {C['success']}{Config.CURRENT_JSON_BASE}.json{C['reset']}
 🔥 {C['warning']}{C['bold']}Activated File{C['reset']}: {C['success']}{Config.CURRENT_ACTIVATED_BASE}.json{C['reset']}{custom_settings}"""

    print(f"{C['c4']}╔══ 🚀 {C['accent']}{C['bold']}SYSTEM INITIALIZATION LOGS{C['reset']}{C['c4']} ═══════════════════════════════════════════╗")
    for log_line in config_text.split('\n'):
        visible_len = len(re.sub(r'\033\[[0-9;]*m', '', log_line))
        pad = max(0, 74 - visible_len)
        print(f"{C['c4']}║{C['reset']}{log_line}{' ' * pad}{C['c4']}║{C['reset']}")
    print(f"{C['c4']}╚═══════════════════════════════════════════════════════════════════════════╝")
    print()

    print(f"\n{C['warning']}⏳ Loading virtual registry variables...{C['reset']}")
    time.sleep(0.5)

    SUCCESS_COUNTER = RARE_COUNTER = COUPLES_COUNTER = 0
    ACTIVATED_COUNTER = FAILED_ACTIVATION_COUNTER = BIO_SET_COUNTER = 0
    Config.FRIEND_REQ_SUCCESS_COUNT = 0
    Config.FRIEND_REQ_FAILED_COUNT = 0
    Config.CLAN_REQ_SUCCESS_COUNT = 0
    Config.CLAN_REQ_FAILED_COUNT = 0
    start_time = time.time()
    threads = []

    global GENERATION_SILENT
    GENERATION_SILENT = True
    print(f"\n{C['primary']}{C['bold']}🚀 Deploying {thread_count} sub-workers in multi-channel loop...{C['reset']}\n")
    for i in range(thread_count):
        t = threading.Thread(target=worker, args=(selected_region, account_count, i+1, is_ghost))
        t.daemon = True
        t.start()
        threads.append(t)

    try:
        while any(t.is_alive() for t in threads):
            time.sleep(1)
            with Config.LOCK:
                if SUCCESS_COUNTER >= account_count:
                    break
    except KeyboardInterrupt:
        EXIT_FLAG = True

    for t in threads:
        t.join(timeout=3)

    GENERATION_SILENT = False
    elapsed = time.time() - start_time
    final_stats = f"""📊 Total Created : {SUCCESS_COUNTER}/{account_count}
💎 Rare Detected : {RARE_COUNTER}
💞 Pairs Matched : {COUPLES_COUNTER}
🔥 TCP Activated : {ACTIVATED_COUNTER}
❌ Sockets Failed: {FAILED_ACTIVATION_COUNTER}
📝 Bio Slices Set: {BIO_SET_COUNTER}
🎭 Emotes Equipped: {SUCCESS_COUNTER if Config.AUTO_EMOTE else 0}
🔌 Req Sent OK   : {Config.FRIEND_REQ_SUCCESS_COUNT}
🔌 Req Sent FAIL : {Config.FRIEND_REQ_FAILED_COUNT}
🛡️ Guild Sent OK  : {Config.CLAN_REQ_SUCCESS_COUNT}
🛡️ Guild Sent FAIL: {Config.CLAN_REQ_FAILED_COUNT}
⏱️  Time Elapsed : {elapsed:.2f}s
⚡ Matrix Speed  : {SUCCESS_COUNTER/elapsed:.2f} acc/s
🔌 Total Socket  : {Config.ATTEMPTS}
👤 Security Level: {Config.USER_LEVEL}"""
    print(VISUAL.create_panel("🎉 CYBER MATRIX INTEGRATION COMPLETE!", final_stats, color="success"))
    input(f"\n{C['warning']}{C['bold']}⏎ Press Enter to exit back to core module...{C['reset']}")

def admin_panel():
    if Config.USER_LEVEL == "USER":
        print_error("Access Denied! Unauthorized client level detected.")
        time.sleep(2); return
    while True:
        VISUAL.show_header(Config.USER_LEVEL)
        credits = CreditEditor.load_credits()
        C = VISUAL.COLORS
        admin_menu = f"""👤 Account Level : {Config.USER_LEVEL}
🔌 active sockets : {API_COUNT}

📝 MATRIX CREDIT MANAGEMENT:
 [1] Edit Primary Credit Signature   (Current: {credits['primary_credit']})
 [2] Edit Telegram Handles           (Current: {credits['telegram1']}, {credits['telegram2']})
 [3] Edit GitHub Repository Link     (Current: {credits['github']})
 [4] Edit Terminal Banner String     (Current: {credits['banner_text'][:25]}...)
 [5] Edit Social Bio String          (Current: {credits['bio_text'][:25]}...)
 [6] Save All Matrix Credit Changes
 [7] Revert to Factory Defaults

⚙️ DYNAMIC GENERATION CONTROLS:
 [8] Edit Default Name Tag Prefix    (Current: {Config.CUSTOM_NAME_PREFIX})
 [9] Edit Default Passcode Prefix    (Current: {Config.CUSTOM_PASS_PREFIX})
 [10] Set ID Rarity Score Level      (Current: {Config.CUSTOM_RARITY_THRESHOLD})
 [11] Adjust Target Limit            (Current: {Config.CUSTOM_TARGET})
 [12] Adjust Active Threads Count    (Current: {Config.MAX_THREADS} / 150 max)
 [13] Set Max Socket Reconnects      (Current: {Config.MAX_RETRIES})

📊 SYSTEM STATUS & RECOVERY:
 [14] Show Real-time API Statistics
 [15] Hard Reset Workspace Directories
 [16] Backup Current Script Code
 [17] Reset System Counters
 [18] Toggle Terminal Debug Logs
 [19] Return to Core Module Menu"""
        if Config.USER_LEVEL == "OWNER":
            admin_menu += "\n\n👑 OWNER SYSTEM INJECTORS:\n [20] Toggle Force Generation Mode\n [21] Toggle Rate Limit Bypass Hooks\n [22] Toggle Priority API Distribution"
        print(VISUAL.create_panel("🔧 ARIYAN ULTIMATE CONTROL MODULE", admin_menu, color='admin'))
        choice = VISUAL.get_input("ADMIN INDEX COMMAND", "Select option key to manipulate matrix:", "admin")

        if choice == "1":
            nc = VISUAL.get_input("PRIMARY CREDIT KEY", "Enter new credit identity label:", "admin")
            if nc:
                credits['primary_credit'] = nc
                CreditEditor.save_credits(credits)
                print_success("Updated!")
            time.sleep(1)
        elif choice == "2":
            t1 = VISUAL.get_input("TELEGRAM CONFIG 1", "Enter Telegram portal 1 string:", "admin")
            t2 = VISUAL.get_input("TELEGRAM CONFIG 2", "Enter Telegram portal 2 string:", "admin")
            if t1 or t2:
                credits['telegram1'] = t1 if t1 else credits['telegram1']
                credits['telegram2'] = t2 if t2 else credits['telegram2']
                CreditEditor.save_credits(credits)
                print_success("Updated!")
            time.sleep(1)
        elif choice == "3":
            ng = VISUAL.get_input("GITHUB REPO INDEX", "Enter Github repository address:", "admin")
            if ng:
                credits['github'] = ng
                CreditEditor.save_credits(credits)
                print_success("Updated!")
            time.sleep(1)
        elif choice == "4":
            nb = VISUAL.get_input("CONSOLE BANNER KEY", "Enter banner string details:", "admin")
            if nb:
                credits['banner_text'] = nb
                CreditEditor.save_credits(credits)
                print_success("Updated!")
            time.sleep(1)
        elif choice == "5":
            nbio = VISUAL.get_input("DEFAULT BIO MATRIX", "Enter bio string sequence:", "admin")
            if nbio:
                credits['bio_text'] = nbio
                Config.BIO_TEXT = nbio
                CreditEditor.save_credits(credits)
                print_success("Updated!")
            time.sleep(1)
        elif choice == "6":
            CreditEditor.save_credits(credits); print_success("Saved!"); time.sleep(1)
        elif choice == "7":
            d = {"primary_credit":"Ariyan","github":"https://github.com/Ariyan",
                 "telegram1":"@Ariyan","telegram2":"@Ariyan","display_name":"Ariyan",
                 "banner_text":"⚡ POWERED BY ARIYAN ⚡",
                 "footer_text":"👤 CREDIT: Ariyan | TELEGRAM: @Ariyan,@Ariyan | GITHUB: Ariyan",
                 "bio_text":"[FF0000]🌈[FF7700]A[FFFF00]R[00FF00]I[00BFFF]Y[8B00FF]A[FF0000]N[FFFF00]_[00FF00]C[00BFFF]O[8B00FF]D[FF0000]E [FF7700]C[FFFF00]R[00FF00]E[00BFFF]A[8B00FF]T[FF0000]I[FF7700]O[FFFF00]N[FF0000]🌈"}
            CreditEditor.save_credits(d); Config.BIO_TEXT = d['bio_text']
            print_success("Defaults restored!"); time.sleep(1)
        elif choice == "8":
            np = VISUAL.get_input("USERNAME NAME TAG", "Enter default username prefix:", "admin")
            if np:
                Config.CUSTOM_NAME_PREFIX = np
                print_success(f"Set: {Config.CUSTOM_NAME_PREFIX}")
            time.sleep(1)
        elif choice == "9":
            pp = VISUAL.get_input("PASSWORD PREFIX TAG", "Enter default pass prefix:", "admin")
            if pp:
                Config.CUSTOM_PASS_PREFIX = pp
                print_success(f"Set: {Config.CUSTOM_PASS_PREFIX}")
            time.sleep(1)
        elif choice == "10":
            try:
                n_str = VISUAL.get_input("RARITY INDEX LIMIT", "Set rarity index limit range (1-10):", "admin")
                if n_str.isdigit():
                    n = int(n_str)
                    if 1 <= n <= 10: 
                        Config.CUSTOM_RARITY_THRESHOLD = n
                        print_success(f"Set: {n}")
                    else: 
                        print_error("Must be 1–10")
            except: 
                print_error("Invalid input")
            time.sleep(1)
        elif choice == "11":
            try: 
                tgt_str = VISUAL.get_input("MAX TARGET COUNT", "Enter target limit threshold:", "admin")
                if tgt_str.isdigit():
                    Config.CUSTOM_TARGET = int(tgt_str)
                    print_success(f"Set: {Config.CUSTOM_TARGET}")
            except: 
                print_error("Invalid")
            time.sleep(1)
        elif choice == "12":
            try:
                th_str = VISUAL.get_input("ACTIVE THREAD CONFIG", "Enter thread allocations (1-150):", "admin")
                if th_str.isdigit():
                    n = int(th_str)
                    if 1 <= n <= 150:
                        Config.MAX_THREADS = n
                        print_success(f"Set: {n}")
                    else: 
                        print_error("Must be 1–150")
            except: 
                print_error("Invalid")
            time.sleep(1)
        elif choice == "13":
            try:
                rt_str = VISUAL.get_input("MAX RECONNECT CHANNELS", "Enter max socket retries (1-20):", "admin")
                if rt_str.isdigit():
                    n = int(rt_str)
                    if 1 <= n <= 20: 
                        Config.MAX_RETRIES = n
                        print_success(f"Set: {n}")
                    else: 
                        print_error("Must be 1–20")
            except: 
                print_error("Invalid")
            time.sleep(1)
        elif choice == "14":
            sr = (SUCCESS_COUNTER / Config.ATTEMPTS * 100) if Config.ATTEMPTS > 0 else 0
            st = f"Total Sockets: {Config.ATTEMPTS} | Success: {SUCCESS_COUNTER} | Rejected: {Config.ATTEMPTS-SUCCESS_COUNTER} | Success Ratio: {sr:.1f}% | Active API nodes: {API_COUNT}"
            print(VISUAL.create_panel("📊 CORE ENDPOINT STATISTICS", st, color="admin"))
            input(f"\n{C['warning']}⏎ Press Enter to return...{C['reset']}")
        elif choice == "15":
            confirm = VISUAL.get_input("HARD WORKSPACE PURGE", "Type CONFIRM to delete all directory caches:", "error")
            if confirm == "CONFIRM":
                shutil.rmtree(Config.BASE_FOLDER)
                Config.create_folders()
                print_success("Workspace directory trees re-initialized successfully!")
            time.sleep(2)
        elif choice == "16":
            bp = CreditEditor.backup_current_file()
            print_success(f"Security backup generated successfully: {bp}") if bp else print_error("Backup engine failure!")
            time.sleep(2)
        elif choice == "17":
            Config.SUCCESS = Config.RARE = Config.COUPLES = Config.ACTIVATED = Config.FAILED = Config.BIO = Config.ATTEMPTS = 0
            print_success("Matrix variables and counts reset successfully!"); time.sleep(1)
        elif choice == "18":
            Config.DEBUG_MODE = not Config.DEBUG_MODE
            print_success(f"System Terminal Debug: {'ENABLED' if Config.DEBUG_MODE else 'DISABLED'}"); time.sleep(1)
        elif choice == "19":
            break
        elif choice == "20" and Config.USER_LEVEL == "OWNER":
            Config.FORCE_GENERATION = not Config.FORCE_GENERATION
            print_success(f"Force generation hooks: {'ACTIVE' if Config.FORCE_GENERATION else 'INACTIVE'}"); time.sleep(1)
        elif choice == "21" and Config.USER_LEVEL == "OWNER":
            Config.BYPASS_RATE_LIMIT = not Config.BYPASS_RATE_LIMIT
            print_success(f"Bypass rate limits: {'ACTIVE' if Config.BYPASS_RATE_LIMIT else 'INACTIVE'}"); time.sleep(1)
        elif choice == "22" and Config.USER_LEVEL == "OWNER":
            Config.CUSTOM_API_PRIORITY = not Config.CUSTOM_API_PRIORITY
            print_success(f"Custom api priorities: {'ACTIVE' if Config.CUSTOM_API_PRIORITY else 'INACTIVE'}"); time.sleep(1)
        else:
            print_error("Invalid index key or client authorization failure."); time.sleep(1)

def view_saved_accounts():
    VISUAL.show_header(Config.USER_LEVEL)
    folders = [Config.ACCOUNTS_FOLDER, Config.ACTIVATED_FOLDER,
               Config.RARE_ACCOUNTS_FOLDER, Config.COUPLES_ACCOUNTS_FOLDER]
    total = 0; results = ""
    for folder in folders:
        if os.path.exists(folder):
            for file in [f for f in os.listdir(folder) if f.endswith('.json')]:
                filepath = os.path.join(folder, file)
                try:
                    data = safe_json_load(filepath, [])
                    results += f" 📂 {os.path.basename(folder)}/{file:<32} » Count: {len(data)} records\n"
                    total += len(data)
                except: pass
    results += f"\n📊 GLOBAL DIRECTORY REGISTRY TOTAL: {total} accounts synchronized"
    print(VISUAL.create_panel("📁 MATRIX DATABASE RECOVERY", results, color="secondary"))
    input(f"\n{VISUAL.COLORS['warning']}{VISUAL.COLORS['bold']}⏎ Press Enter to exit view registry...{VISUAL.COLORS['reset']}")

# =============================================================================
# 🚀 STANDALONE BOT HOSTING SYSTEM (FROM main.py)
# =============================================================================

# Global bot server tracking
BOT_SERVERS = {}

def save_ariyan_vip_txt(uid, password):
    """Saves successful request-executing accounts dynamically to VIP file"""
    try:
        filepath = os.path.join(Config.ACCOUNTS_FOLDER, "ariyan-vip.txt")
        already_exists = False
        if os.path.exists(filepath):
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                if f"{uid}:{password}" in content:
                    already_exists = True
        
        if not already_exists:
            with get_file_lock(filepath):
                with open(filepath, "a", encoding="utf-8") as f:
                    f.write(f"{uid}:{password}\n")
    except:
        pass

def load_accounts_from_file(filepath):
    """Parses credential accounts file smoothly"""
    accounts = []
    if os.path.exists(filepath):
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    if not line: continue
                    if ":" in line:
                        parts = line.split(":", 1)
                        if len(parts) == 2:
                            accounts.append({"uid": parts[0].strip(), "password": parts[1].strip()})
        except Exception as e:
            debug_print(f"Error loading {filepath}: {e}")
    return accounts

def run_single_bot_server(slot_id, account, send_friend, target_uid, send_guild, target_guild):
    global BOT_SERVERS, EXIT_FLAG
    slot = BOT_SERVERS[slot_id]
    slot["status"] = "Starting"
    slot["uid"] = account["uid"]
    slot["pwd"] = account["password"]
    slot["account_id"] = account["uid"]
    slot["logs"] = ["Booting client..."]

    bot_dir = os.path.join(Config.CURRENT_DIR, f"Ariyan_VIP_{slot_id}")
    github_repo = "https://github.com/Ariyan20267/Ariyan_bot.git"

    if not os.path.exists(bot_dir):
        slot["status"] = "Cloning"
        slot["logs"] = ["Cloning repo..."]
        res = subprocess.run(["git", "clone", "--depth", "1", github_repo, bot_dir], capture_output=True)
        if res.returncode != 0:
            slot["status"] = "Clone Fail"
            slot["logs"] = ["Clone aborted."]
            slot["online"] = False
            return

    session = requests.Session()
    adapter = requests.adapters.HTTPAdapter(pool_connections=1, pool_maxsize=1, max_retries=1)
    session.mount("https://", adapter)
    session.mount("http://", adapter)

    # Perform network logins in background non-blockingly to send requests successfully
    try:
        access_token, open_id = _bio_guest_login(account["uid"], account["password"])
        if access_token and open_id:
            login_result = _perform_major_login_sync(account["uid"], account["password"], access_token, open_id, "IND", session)
            jwt_token = login_result.get("jwt_token", "")
            account_id = login_result.get("account_id", "N/A")
            ml_url = login_result.get("ml_url", "")

            if jwt_token and account_id != "N/A":
                slot["account_id"] = account_id
                
                # Perform Friends and Guild/Clan requests instantly
                friend_ok = False
                guild_ok = False

                if send_friend and target_uid:
                    slot["logs"] = ["Snd Friend..."]
                    st = send_friend_request(session, account_id, target_uid, jwt_token, ml_url)
                    if st == "SUCCESS": friend_ok = True

                if send_guild and target_guild:
                    slot["logs"] = ["Joining Guild..."]
                    st = send_clan_join_request(session, account_id, target_guild, jwt_token, ml_url)
                    if st == "SUCCESS": guild_ok = True

                # Save successful credentials dynamically inside ariyan-vip.txt
                if (send_friend and friend_ok) or (send_guild and guild_ok) or (not send_friend and not send_guild):
                    save_ariyan_vip_txt(account["uid"], account["password"])
    except Exception as e:
        debug_print(f"Pre-login process skipped/failed: {e}")

    try:
        # Write Garena credentials inside bot directory exactly like s.py
        ariyan_txt_path = os.path.join(bot_dir, "ARIYAN.txt")
        with open(ariyan_txt_path, 'w', encoding='utf-8') as f:
            json.dump({account["uid"]: account["password"]}, f, indent=4)

        slot["logs"] = ["Launching main..."]

        # Launch Bot repository using sub-processes to run main.py inside each directory
        slot["process"] = subprocess.Popen(
            [sys.executable, "-u", "main.py"],
            cwd=bot_dir,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1
        )
        
        slot["status"] = "Online"
        slot["online"] = True
        slot["logs"] = ["Active Running"]

        # Capture the subprocess outputs/logs line by line safely
        for line in iter(slot["process"].stdout.readline, ''):
            if EXIT_FLAG or not slot["online"] or slot["status"] != "Online":
                break
            line_str = line.strip()
            if line_str:
                # Clean Garena/Rich console Ansi color sequences cleanly
                ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-9?]*[ -/]*[@-~])')
                clean_line = ansi_escape.sub('', line_str)
                slot["logs"].append(clean_line)
                if len(slot["logs"]) > 20:
                    slot["logs"].pop(0)

        slot["process"].wait()
        slot["status"] = "Stopped"
        slot["online"] = False
        slot["logs"].append("Engine Exited.")

    except Exception as e:
        slot["status"] = "Error"
        slot["logs"] = [f"Err: {str(e)[:15]}"]
        slot["online"] = False

def display_sequential_booting(num_bots):
    """Clean terminal sequential display during boot phase"""
    VISUAL.clear()
    C = VISUAL.COLORS
    print(f"{C['primary']}{C['bold']}==============================================================")
    print("🚀  ARIYAN SYSTEM: INITIATING SEQUENTIAL WORKER HOSTS")
    print("==============================================================\n" + C['reset'])
    for idx in range(1, num_bots + 1):
        bid = str(idx)
        b = BOT_SERVERS.get(bid, {"status": "Offline", "logs": ["Inactive"]})
        last_log = b["logs"][-1] if b["logs"] else "Initializing..."
        color = C['success'] if b["status"] == "Online" else C['warning'] if b["status"] in ["Cloning", "Starting"] else C['error']
        print(f" {C['accent']}[S#{idx:02d}]{C['reset']} Status: {color}{b['status']:<10}{C['reset']} Logs: {C['dim']}{last_log}{C['reset']}")
    print()

def show_enlarged_log_room(idx, num_bots):
    """Enlarged box room showing up to 5 lines of detailed real-time stdout logs"""
    VISUAL.clear()
    C = VISUAL.COLORS
    bid = str(idx)
    b = BOT_SERVERS.get(bid, {"status": "Offline", "online": False, "account_id": "N/A", "logs": ["Inactive"]})
    
    if b["status"] == "Online": color = C['success']
    elif b["status"] in ["Cloning", "Starting"]: color = C['warning']
    else: color = C['error']

    status_str = b["status"][:18]
    uid_str = b["account_id"][:18]
    
    # Format and pad logs up to 4 lines vertically
    raw_logs = b["logs"][-4:]
    while len(raw_logs) < 4:
        raw_logs.insert(0, "")
    
    log1 = raw_logs[0][:30]
    log2 = raw_logs[1][:30]
    log3 = raw_logs[2][:30]
    log4 = raw_logs[3][:30]

    # Adjusted to exactly 34 chars inner width
    print(f"\n  {color}╔═════════════ [S#{idx:02d} LOG ROOM] ═════════════╗{C['reset']}")
    print(f"  {color}║{C['reset']} State: {C['accent']}{status_str:<18}{C['reset']}{color}        ║{C['reset']}")
    print(f"  {color}║{C['reset']} ID: {C['primary']}{uid_str:<18}{C['reset']}{color}           ║{C['reset']}")
    print(f"  {color}║ ──────────────────────────────── ║{C['reset']}")
    print(f"  {color}║{C['reset']} {C['secondary']}{log1:<32}{C['reset']}{color} ║{C['reset']}")
    print(f"  {color}║{C['reset']} {C['secondary']}{log2:<32}{C['reset']}{color} ║{C['reset']}")
    print(f"  {color}║{C['reset']} {C['secondary']}{log3:<32}{C['reset']}{color} ║{C['reset']}")
    print(f"  {color}║{C['reset']} {C['secondary']}{log4:<32}{C['reset']}{color} ║{C['reset']}")
    print(f"  {color}╚══════════════════════════════════╝{C['reset']}")
    print(f"\n  {C['warning']}⏱️  Displaying live console log frame for exactly 3 seconds...{C['reset']}")

def display_interactive_control_deck(num_bots):
    """Visual menu listing active online bots with account identifiers"""
    VISUAL.clear()
    C = VISUAL.COLORS
    W = shutil.get_terminal_size().columns
    print(f"{C['c1']}{C['bold']}" + "=" * W)
    print("🚀  ARIYAN SYSTEM: ACTIVE CLOUD DESK CONTROLLER".center(W))
    print("=" * W + f"{C['reset']}\n")

    print(f" {C['accent']}{C['bold']}ACTIVE WORKERS DETECTED:{C['reset']}\n")
    for idx in range(1, num_bots + 1):
        bid = str(idx)
        b = BOT_SERVERS.get(bid, {"status": "Offline", "account_id": "N/A"})
        color = C['success'] if b["status"] == "Online" else C['warning'] if b["status"] in ["Cloning", "Starting"] else C['error']
        print(f"  {C['primary']}[{idx:02d}]{C['reset']} Bot Slot {idx:02d} » ID: {C['accent']}{b['account_id']:<15}{C['reset']} » {color}{b['status']}{C['reset']}")
    print(f"\n  {C['primary']}[Q]{C['reset']} {C['error']}Shut Down Active Bot Servers & Exit{C['reset']}\n")

def cleanup_bot_folders(active_indices):
    """Loops and dynamically removes all selected virtual server slots on termination"""
    C = VISUAL.COLORS
    print(f"\n {C['warning']}🧹 Sweeping local memory and purging selected bot workspaces...{C['reset']}")
    for idx in active_indices:
        bot_dir = os.path.join(Config.CURRENT_DIR, f"Ariyan_VIP_{idx}")
        if os.path.exists(bot_dir):
            try:
                shutil.rmtree(bot_dir)
            except:
                pass
    print(f" {C['success']}✅ Workspace memory slots cleared successfully.{C['reset']}")

def run_hosting_system():
    global BOT_SERVERS, EXIT_FLAG
    C = VISUAL.COLORS
    VISUAL.clear()
    
    os.makedirs(Config.ACCOUNTS_FOLDER, exist_ok=True)
    
    # Interactive File Selector Prompt
    print(f"  {C['primary']}[1]{C['reset']} Load credentials from {C['success']}ariyan.txt{C['reset']} (Generator accounts)")
    print(f"  {C['primary']}[2]{C['reset']} Load credentials from {C['success']}ariyan-vip.txt{C['reset']} (VIP saved accounts)")
    choice = VISUAL.get_input("SELECT CREDENTIAL SOURCE", "Enter [1] or [2]:", "primary")

    if choice == "2":
        file_path = os.path.join(Config.ACCOUNTS_FOLDER, "ariyan-vip.txt")
    else:
        file_path = os.path.join(Config.ACCOUNTS_FOLDER, "ariyan.txt")

    accounts = load_accounts_from_file(file_path)
    if not accounts:
        # Fallback to VIP if original generator is missing
        file_path = os.path.join(Config.ACCOUNTS_FOLDER, "ariyan-vip.txt")
        accounts = load_accounts_from_file(file_path)

    if not accounts:
        print(f"{C['error']}❌ No account credentials found inside 'ariyan.txt' or 'ariyan-vip.txt'!{C['reset']}")
        time.sleep(2.5)
        return

    # Select bot limit cleanly (Max 15)
    while True:
        bot_qty_input = VISUAL.get_input("BOT RUN QUANTITY", "Enter number of bots to deploy (Max 15):", "primary")
        if bot_qty_input.isdigit():
            num_bots = int(bot_qty_input)
            if 1 <= num_bots <= 15:
                break
            else:
                print(f"{C['error']}Quantity must be between 1 and 15!{C['reset']}")
        else:
            print(f"{C['error']}Please enter a valid number!{C['reset']}")

    # Cyclic account allocation (Modulo cycle) to allow scaling bots beyond file counts cleanly without crashing
    selected_accounts = []
    for i in range(num_bots):
        selected_accounts.append(accounts[i % len(accounts)])
        
    active_indices = list(range(1, num_bots + 1))

    # Pre-clear only directories of slots we are running
    cleanup_bot_folders(active_indices)

    # Ask Garena operations
    send_friend = False
    target_uid = 0
    friend_choice = VISUAL.get_input("FRIEND REQUEST MODULE", "Enable Garena Friend Requests? (Y/N):", "secondary").strip().upper()
    if friend_choice == 'Y':
        send_friend = True
        while True:
            target_uid_input = VISUAL.get_input("TARGET USER UID", "Enter Target Player UID:", "primary")
            if target_uid_input.isdigit() and int(target_uid_input) > 0:
                target_uid = int(target_uid_input)
                break
            else:
                print(f"{C['error']}Invalid UID Code!{C['reset']}")

    send_guild = False
    target_guild = 0
    guild_choice = VISUAL.get_input("GUILD JOIN MODULE", "Enable Garena Guild Join Requests? (Y/N):", "secondary").strip().upper()
    if guild_choice == 'Y':
        send_guild = True
        while True:
            target_guild_input = VISUAL.get_input("TARGET CLAN GUILD ID", "Enter Target Guild ID:", "primary")
            if target_guild_input.isdigit() and int(target_guild_input) > 0:
                target_guild = int(target_guild_input)
                break
            else:
                print(f"{C['error']}Invalid Guild ID!{C['reset']}")

    # Setup active structures
    BOT_SERVERS = {
        str(i): {
            "uid": "N/A", "pwd": "N/A", "status": "Offline", 
            "logs": ["Booting..."], "online": False, "account_id": "N/A"
        } for i in active_indices
    }

    # Stagger boot sequentially
    for idx in active_indices:
        acc = selected_accounts[idx - 1]
        slot_id = str(idx)
        t = threading.Thread(
            target=run_single_bot_server,
            args=(slot_id, acc, send_friend, target_uid, send_guild, target_guild),
            daemon=True
        )
        t.start()

    # Step 1: Wait & show sequential loading screen until all bots booted
    all_ready = False
    while not all_ready:
        display_sequential_booting(num_bots)
        time.sleep(1.5)
        with threading.Lock():
            ready_count = sum(1 for i in active_indices if BOT_SERVERS[str(i)]["status"] in ["Online", "Auth Fail", "Login Fail", "Error", "Stopped"])
            if ready_count == num_bots:
                all_ready = True

    # Step 2: Main interactive selection desk
    try:
        while True:
            display_interactive_control_deck(num_bots)
            choice = input(f"  {C['c4']}➤ {C['success']}{C['bold']}SELECT SLOT# TO VIEW LOGS (Or Q to Exit){C['reset']} {C['c6']}» {C['reset']}").strip().upper()
            if choice == 'Q':
                raise KeyboardInterrupt
            elif choice.isdigit() and 1 <= int(choice) <= num_bots:
                show_enlarged_log_room(int(choice), num_bots)
                time.sleep(3.0)
            else:
                print(f"  {C['error']}❌ Invalid Option!{C['reset']}")
                time.sleep(1)
    except KeyboardInterrupt:
        print(f"\n{C['error']}⚠️ Shutdown sequence triggered. Deactivating workers...{C['reset']}")
        EXIT_FLAG = True
        for idx in active_indices:
            bid = str(idx)
            if bid in BOT_SERVERS:
                BOT_SERVERS[bid]["status"] = "Offline"
                BOT_SERVERS[bid]["online"] = False
                proc = BOT_SERVERS[bid].get("process")
                if proc:
                    try: proc.kill()
                    except: pass
        time.sleep(1)
        cleanup_bot_folders(active_indices)
        time.sleep(1)

# =============================================================================
# 📌 MAIN MENU (Option 3 removed - Display Runtime Metrics)
# =============================================================================

def main_menu():
    Config.create_folders()
    while True:
        VISUAL.show_header(Config.USER_LEVEL)
        C = VISUAL.COLORS
        
        # Creating the main panel with individual boxes
        menu_options = [
            ("1", "🚀", "Deploy Generation Loop", "green"),
            ("2", "📁", "Read Local Registry Directories", "blue"),
            ("3", "🤖", "Launch Bot Hosting System", "purple"),  # Replaced Stats with Bot Hosting
            ("4", "💡", "Inspect System Metadata", "purple")
        ]
        
        # Add admin options based on user level
        if Config.USER_LEVEL in ["ADMIN", "OWNER"]:
            menu_options.append(("5", "🔧", "Access Control Panel", "cyan"))
            menu_options.append(("6", "🚪", "Safely Terminate Connection", "red"))
        else:
            menu_options.append(("5", "🚪", "Safely Terminate Connection", "red"))
        
        # Build the menu display with individual colored boxes
        menu_display = []
        for num, icon, text, color in menu_options:
            box = create_menu_box(num, icon, text, color)
            menu_display.append(box)
        
        # Join all boxes with proper spacing
        menu_content = '\n'.join(menu_display)
        
        print(VISUAL.create_panel("📌 CORE APPLICATION MATRIX", menu_content, color="primary"))
        
        choice = VISUAL.get_input("SYSTEM PORTAL NAVIGATION", "⏤꯭✮͢𓆩𝐂𝐇𝐎𝐎𝐒𝐄 𝐘𝐎𝐔𝐑 𝐎𝐏𝐓𝐈𝐎𝐍𓆪-:)💙", "primary")
        
        if choice == "1":   generate_accounts_flow()
        elif choice == "2": view_saved_accounts()
        elif choice == "3": run_hosting_system()  # Now calls the bot hosting system
        elif choice == "4": about()
        elif choice == "5":
            if Config.USER_LEVEL in ["ADMIN","OWNER"]: admin_panel()
            else: print(f"\n{C['primary']}{C['bold']}👋 System shutdown initiated. Goodbye!{C['reset']}"); sys.exit(0)
        elif choice == "6" and Config.USER_LEVEL in ["ADMIN","OWNER"]:
            print(f"\n{C['primary']}{C['bold']}👋 System shutdown initiated. Goodbye!{C['reset']}"); sys.exit(0)
        else:
            print_error("Invalid index entered! Try again."); time.sleep(1)

# =============================================================================
# 🚀 MAIN EXECUTION
# =============================================================================

if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        safe_exit()
    except Exception as e:
        print_error(f"Matrix runtime failure: {e}")
        time.sleep(2)
        os.execv(sys.executable, [sys.executable] + sys.argv)