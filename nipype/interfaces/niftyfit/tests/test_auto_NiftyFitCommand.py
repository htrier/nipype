# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..base import NiftyFitCommand


def test_NiftyFitCommand_inputs():
    input_map = dict(
        args=dict(argstr="%s",), environ=dict(nohash=True, usedefault=True,),
    )
    inputs = NiftyFitCommand.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
