.section .data
    fmt: .string "%1211u\n"
 
.section .text
    .global _start
_start:
    mov $50, %rcx
    mov $1, %rax
    mov $1, %rbx
 
fibloop:
    push %rax
    push %rcx

    mov $fmt, %rdi
    mov %rax, %rsi
    xor %rax, %rax
    call printf
   
   pop %rcx
   pop %rax

   mov %rax, %rdx
   mov %rbx, %rax
   add %rdx, %rbx
   
   dec %rcx
   jnz fibloop

   mov $60, %rax
   xor %rdi, %rdi
   syscall
