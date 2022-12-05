# graduation_thesis

## environment construction

with reference to [web site](https://touch-sp.hatenablog.com/entry/2022/10/11/145610)
```bash
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
```
### download sd-v1-d.ckpt
install [here](https://huggingface.co/CompVis/stable-diffusion-v-1-4-original)

Move to 'models/ldm/stable-diffusion-v1/'

## operation check

Change DEFAULT_CKPT in optimized_text2img.py from "models/ldm/stable-diffusion-v1/model.ckpt" to "models/ldm/stable-diffusion-v1/sd-v1-4.ckpt"
```python
cd ~/デスクトップ/stable-diffusion/
python optimizedSD/optimized_txt2img.py --prompt "a photograph of an astronaut riding a horse"
```