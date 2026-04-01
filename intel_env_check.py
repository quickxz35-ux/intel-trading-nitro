import sys
import os

def check_optimizations():
    print("--- 🏎️ INTEL TRADING NITRO: ENVIRONMENT CHECK ---")
    
    # 1. Check Sklearn-Intelex
    try:
        from sklearnex import is_patched
        print(f"[OK] Scikit-Learn Intelex: {'PATCHED' if is_patched() else 'Loaded but not patched'}")
    except ImportError:
        print("[!!] Scikit-Learn Intelex: NOT INSTALLED")

    # 2. Check Modin
    try:
        import modin
        print(f"[OK] Modin (Parallel Pandas): INSTALLED (v{modin.__version__})")
    except ImportError:
        print("[!!] Modin: NOT INSTALLED")

    # 3. Check OpenVINO
    try:
        import openvino
        print(f"[OK] OpenVINO: INSTALLED")
    except ImportError:
        print("[!!] OpenVINO: NOT INSTALLED")

    # 4. Check Chronos Toolkit Folder
    if os.path.exists('chronos_toolkit'):
        print("[OK] Chronos Toolkit: CLONED (LOCAL)")
    else:
        print("[!!] Chronos Toolkit: FOLDER MISSING")

if __name__ == "__main__":
    check_optimizations()
