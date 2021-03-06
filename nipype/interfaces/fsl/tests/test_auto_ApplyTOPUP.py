# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..epi import ApplyTOPUP


def test_ApplyTOPUP_inputs():
    input_map = dict(
        args=dict(argstr="%s",),
        datatype=dict(argstr="-d=%s",),
        encoding_file=dict(argstr="--datain=%s", extensions=None, mandatory=True,),
        environ=dict(nohash=True, usedefault=True,),
        in_files=dict(argstr="--imain=%s", mandatory=True, sep=",",),
        in_index=dict(argstr="--inindex=%s", sep=",",),
        in_topup_fieldcoef=dict(
            argstr="--topup=%s",
            copyfile=False,
            extensions=None,
            requires=["in_topup_movpar"],
        ),
        in_topup_movpar=dict(
            copyfile=False, extensions=None, requires=["in_topup_fieldcoef"],
        ),
        interp=dict(argstr="--interp=%s",),
        method=dict(argstr="--method=%s",),
        out_corrected=dict(
            argstr="--out=%s",
            extensions=None,
            name_source=["in_files"],
            name_template="%s_corrected",
        ),
        output_type=dict(),
    )
    inputs = ApplyTOPUP.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_ApplyTOPUP_outputs():
    output_map = dict(out_corrected=dict(extensions=None,),)
    outputs = ApplyTOPUP.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
