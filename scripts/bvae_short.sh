cd ..


python /root/projects/pytorch_integrated_cell/train_model.py \
	--gpu_ids $1 \
	--save_dir ./results/bvae_short \
        --data_save_path ./results/data.pyt \
	--lrEnc 2E-4 --lrDec 2E-4 \
	--model_name vaaegan3D \
	--train_module bvae \
	--kwargs_optim '{"betas": [0.9, 0.999]}' \
	--imdir /root/results/ipp/ipp_17_10_25 \
	--dataProvider DataProvider3Dh5 \
	--saveStateIter 1 --saveProgressIter 1 \
	--channels_pt1 0 2 --channels_pt2 0 1 2 \
	--batch_size 16  \
	--nlatentdim 128 \
	--nepochs 5 \
	--nepochs_pt2 5 \
	--ndat 32 \
	--overwrite_opts True \
