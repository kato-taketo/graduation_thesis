# graduation_thesis

## first step

with reference to [web site](https://touch-sp.hatenablog.com/entry/2022/10/11/145610)
```python
# Virtual environment construction
python -m venv ~/venv/stable-diffusion
source ~/venv/stable-diffusion/bin/activate
pip install torch==1.11.0+cu113 torchvision==0.12.0+cu113 --extra-index-url https://download.pytorch.org/whl/cu113
pip install -r https://raw.githubusercontent.com/dai-ichiro/env4stable-diffusion/main/requirements4OptimizedSD.txt

# git clone optimized-stable-diffusion
git clone https://github.com/basujindal/stable-diffusion.git

# make directory
cd stable-diffusion
mkdir -p models/ldm/stable-diffusion-v1/
cd optimizedSD

# download sd-v1-d.ckpt
https://huggingface.co/CompVis/stable-diffusion-v-1-4-original
Move to 'models/ldm/stable-diffusion-v1/'
```