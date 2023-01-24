section .data
    prompt db "Please enter your name: ", 0
    name db 100
    hello db "Hello, ", 0
    endl db 10, 0

section .text
    global _start

_start:
    ; Print the prompt
    mov eax, 4
    mov ebx, 1
    mov ecx, prompt
    mov edx, 14
    int 0x80

    ; Read the user's name
    mov eax, 3
    mov ebx, 0
    mov ecx, name
    mov edx, 100
    int 0x80

    ; Print the "Hello, " message
    mov eax, 4
    mov ebx, 1
    mov ecx, hello
    mov edx, 7
    int 0x80

    ; Print the user's name
    mov eax, 4
    mov ebx, 1
    mov ecx, name
    mov edx, 100
    int 0x80

    ; Print a newline
    mov eax, 4
    mov ebx, 1
    mov ecx, endl
    mov edx, 2
    int 0x80

    ; Exit the program
    mov eax, 1
    xor ebx, ebx
    int 0x80
