%.bin:%.asm
	nasm $< -o $@
	
os.img: boot.bin
	dd if=boot.bin of=os.img bs=512 count=4 conv=notrunc
	
.PHONY:qemu



qemu:os.img
	sudo qemu-system-i386 ~/nasm/os.img





.PHONY:clean
clean:
	rm  *.bin os.img
