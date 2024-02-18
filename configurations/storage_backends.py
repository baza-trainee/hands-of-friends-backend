from whitenoise.storage import CompressedManifestStaticFilesStorage


class ForgivingCompressedManifestStaticFilesStorage(
    CompressedManifestStaticFilesStorage
):
    def hashed_name(self, name, content=None, **kwargs):
        try:
            return super().hashed_name(name, content, **kwargs)
        except ValueError:
            return name
