from testsuite_support.utils import run_tool, gprbuild, runcross, contents_of


for boot_mem in ['flash', 'sram', 'ccm']:

    run_tool(['-P', 'prj.gpr', '-XBOOT_MEM=%s' % boot_mem,
              '-s', 'src/crt0.S', '-l', 'src/linker.ld'])

    gprbuild(['-f', '-P', 'prj.gpr', '-XBOOT_MEM=%s' % boot_mem])

    runcross('arm-elf', 'qemu-stm32', 'obj/main', output='runcross.out')

    print(contents_of('runcross.out'))
