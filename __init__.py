NODE_CLASS_MAPPINGS = {
    "GRPulidFluxModelLoader": GRPulidFluxModelLoader,
    "GRPulidFluxInsightFaceLoader": GRPulidFluxInsightFaceLoader,
    "GRPulidFluxEvaClipLoader": GRPulidFluxEvaClipLoader,
    "GRApplyPulidFlux": GRApplyPulidFlux,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "GRPulidFluxModelLoader": "Load PuLID Flux Model GR",
    "GRPulidFluxInsightFaceLoader": "Load InsightFace (PuLID Flux) GR",
    "GRPulidFluxEvaClipLoader": "Load Eva Clip (PuLID Flux) GR",
    "GRApplyPulidFlux": "Apply PuLID Flux GR",
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']
