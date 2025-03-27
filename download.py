from huggingface_hub import snapshot_download

repo_id_1 = "stable-diffusion-v1-5/stable-diffusion-v1-5"
local_dir_1 = "./checkpoints/StableDiffusion"
snapshot_download(
    repo_id=repo_id_1,
    local_dir=local_dir_1,
    repo_type="model",
    revision="main",
    force_download=True,
    ignore_patterns=["*.safetensors", "*.fp16.*"],
)


repo_id_2 = "openai/clip-vit-large-patch14"
local_dir_2 = "./checkpoints/models/clip-vit-large-patch14"
snapshot_download(
    repo_id=repo_id_2,
    local_dir=local_dir_2,
    repo_type="model",
    revision="main",
    force_download=True,
    ignore_patterns=["*.safetensors", "*.fp16.*"],
)


repo_id_3 = "lllyasviel/control_v11p_sd15_lineart"
local_dir_3 = "./checkpoints/models/control_v11p_sd15_lineart"
snapshot_download(
    repo_id=repo_id_3,
    local_dir=local_dir_3,
    repo_type="model",
    revision="main",
    force_download=True,
    ignore_patterns=["*.safetensors", "*.fp16.*"],
)

repo_id_4 = "Johanan0528/MangaNinjia"
local_dir_4 = "./checkpoints/MangaNinjia"
snapshot_download(
    repo_id=repo_id_4,
    local_dir=local_dir_4,
    repo_type="model",
    revision="main",
    force_download=True,
)