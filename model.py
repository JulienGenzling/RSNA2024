import torch
import timm_3d 
import torch.nn as nn

from config import Config

class GradingModel(nn.Module):
    def __init__(self,
                 backbone,
                 in_chans=3,
                 out_classes=5,
                 cutpoint_margin=0):
        super(GradingModel, self).__init__()

        self.config = timm_3d.models.maxxvit.model_cfgs[backbone]
        self.config.conv_cfg.downsample_pool_type = "max"
        self.config.conv_cfg.pool_type = "max"

        self.backbone = timm_3d.models.MaxxVit(
            img_size=Config.vol_size,
            in_chans=in_chans,
            num_classes=out_classes,
            drop_rate=Config.drop_rate,
            drop_path_rate=Config.drop_rate_last,
            cfg=self.config
        )
        self.backbone.head.drop = nn.Dropout(p=Config.drop_rate_last)
        head_in_dim = self.backbone.head.fc.in_features
        self.backbone.head.fc = nn.Identity()

        self.num_classes = out_classes

        self.logits = nn.Linear(head_in_dim, self.num_classes)
    
    def extract_features(self, x):
        return self.backbone(x)
    
    def forward(self, x):
        fts = self.extract_features(x)
        return self.logits(fts)