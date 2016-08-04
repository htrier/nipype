# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ....testing import assert_equal
from ..preprocess import Copy


def test_Copy_inputs():
    input_map = dict(args=dict(argstr='%s',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    in_file=dict(argstr='%s',
    copyfile=False,
    mandatory=True,
    position=-2,
    ),
    out_file=dict(argstr='%s',
    name_source='in_file',
    name_template='%s_copy',
    position=-1,
    ),
    outputtype=dict(),
    terminal_output=dict(nohash=True,
    ),
    )
    inputs = Copy.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(inputs.traits()[key], metakey), value


def test_Copy_outputs():
    output_map = dict(out_file=dict(),
    )
    outputs = Copy.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(outputs.traits()[key], metakey), value