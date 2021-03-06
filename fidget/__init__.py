from .patching import Fidget
from .binary_data import BinaryData
from .new_analysis import OffsetAnalysis
from .techniques import FidgetTechnique, FidgetDefaultTechnique

def patch_file(infile, outfile, options):
    fidgetress = Fidget(infile, **options.pop('Fidget', {}))
    fidgetress.patch(**options)
    fidgetress.apply_patches(outfile)
