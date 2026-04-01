# 🏎️ Intel Trading Nitro
Optimized AI Performance Stack for High-Frequency Trading and Bookmap Analysis.

This repository serves as a **State-Record** for AI subagents to understand the local hardware optimizations already configured on this machine.

## 🛠️ Installed Engines
| Engine | Purpose | Performance Gain |
| :--- | :--- | :--- |
| **Modin** | Multi-core Pandas | 4x - 100x Data Loading |
| **Sklearn-Intelex** | Global ML Patch | 10x - 100x Algorithm Speed |
| **BigDL Chronos** | Time-Series Forecasting | SOTA Intel-Optimized Models |
| **Optimum-Intel** | HuggingFace Bridge | Native OpenVINO Inference |
| **NNCF** | Model Compression | INT8/INT4 Quantization |

## ⚙️ Global Optimizations
- **Site-Customize Patch**: `sitecustomize.py` is configured to automatically enable `sklearnex` for all Python processes.
- **Hardware Acceleration**: CPU Runtime for OpenCL and SYCL are verified and active.

## 🧠 For Subagents
If you are an AI agent picking up this project:
1. **Always use Modin**: Use `import modin.pandas as pd` for any tick data processing.
2. **Leverage Chronos**: Look in the local `chronos_toolkit/` folder for pre-baked forecasting algorithms.
3. **OpenVINO First**: Always prefer `OpenVINO` or `IPEX` for model inference to maximize local hardware throughput.
