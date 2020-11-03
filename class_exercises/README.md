# Buffer Overflow

## Description
Buffer overflows are probably one of the most vicious tools available to an attacker. A small honest mistake made by a programmer with SETUID root permissions can mean catastrophe. 

A buffer overflow is
the technique of overwriting machine code with an attackers own code, this occurs when a program takes input from a user in low-level languages such as c, c++ without checking its size. It can be used to gain root access.

To effectively mitigate buffer overflow vulnerabilities, it is important to understand what buffer overflows are, what dangers they pose to your applications, and what techniques attackers use to successfully exploit these vulnerabilities.

## Vulnerability
The simplest and most common buffer overflow is one where the buffer is on the stack. Let's look at an example.
```
#include <signal.h>
#include <stdio.h>
#include <string.h>
int main(){
	char realPassword[20];
	char givenPassword[20];

	strncpy(realPassword, "0xdeadbeef", 20);
	gets(givenPassword);
	
	if (0 == strncmp(givenPassword, realPassword, 20)){
		printf("SUCCESS!\n");
	}else{
		printf("FAILURE!\n");
	}
	raise(SIGINT);
	printf("givenPassword: %s\n", givenPassword);
	printf("realPassword: %s\n", realPassword);
	return 0;
}
```

```
ubuntu@ubuntu:~$ ./example.c
testing
FAILURE!
givenPassword: testing
realPassword: 0xdeadbeef
```
This is exactly as we’d expect. The password we entered does not match the expected password. However, there is a possibility of buffer overflow in this program because the ```gets()``` function does not check the array bounds.

```
ubuntu@ubuntu:~$ gdb example.c
.
.
.
(gdb) run
Starting program: /home/ubuntu/example.c
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
SUCCESS!
givenPassword: aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
realPassword: aaaaaaaaaaaaaaaaaaaa

Program received signal SIGINT, Interrupt.
0x00007ffff7a42428 in __GI_raise (sig=2) at ../sysdeps/unix/sysv/linux/raise.c:54
54	../sysdeps/unix/sysv/linux/raise.c: No such file or directory.
(gdb) info frame
Stack level 0, frame at 0x7fffffffdde0:
 rip = 0x7ffff7a42428 in __GI_raise (../sysdeps/unix/sysv/linux/raise.c:54); saved rip = 0x40072d
 called by frame at 0x7fffffffde30
 source language c.
 Arglist at 0x7fffffffddd0, args: sig=2
 Locals at 0x7fffffffddd0, Previous frame's sp is 0x7fffffffdde0
 Saved registers:
  rip at 0x7fffffffddd8
(gdb) x/200x 0x7fffffffddd0
0x7fffffffddd0:	0x00000000	0x00000000	0x0040072d	0x00000000
0x7fffffffdde0:	0x61616161	0x61616161	0x61616161	0x61616161
0x7fffffffddf0:	0x61616161	0x61616161	0x61616161	0x61616161
0x7fffffffde00:	0x61616161	0x61616161	0x61616161	0x61616161
0x7fffffffde10:	0x61616161	0x00007f00	0x00000000	0x00000000
```
In the above example, the program can be exploited to give an attacker a root privilege, even though the user entered an incorrect password. In this case, the attacker supplied an input with a length greater than the buffer can hold, creating buffer overflow, which overwrote the memory of integer “SUCCESS” Therefore, despite the incorrect ```givenPassword```, the value of ```aaaaaaaaaa...``` became non zero, and an attacker can exploit this vulnerability by using a shellcode to gain root privileges.

## Mitigation 
1. Address space randomization (ASLR)—randomly moves around the address space locations of data regions. Typically, buffer overflow attacks need to know the locality of executable code, and randomizing address spaces makes this virtually impossible.
2. Data execution prevention—flags certain areas of memory as non-executable or executable, which stops an attack from running code in a non-executable region.
3. Structured exception handler overwrite protection (SEHOP)—helps stop malicious code from attacking Structured Exception Handling (SEH), a built-in system for managing hardware and software exceptions. It thus prevents an attacker from being able to make use of the SEH overwrite exploitation technique. At a functional level, an SEH overwrite is achieved using a stack-based buffer overflow to overwrite an exception registration record, stored on a thread’s stack.
4. Avoid functions that do no bounds checking

| Instead Of    | Use           |
| ------------- |:-------------:|
| gets()        | fgets()       | 
| strcpy()      | strncpy()     | 
| strcat()      | strncat()     |
| sprintf()     | bcopy()       |
| scanf()       | bzero()       |
| sscanf()      | memcpy(), memset()|
5. Be especially careful programming and/or installing setuid root programs and programs that run as root. These are the programs that allow an attacker to acquire a root shell.
6. Be careful when using for and while loops that copy data from one variable to another. Make sure the bounds are checked.
7. Review legacy software code for security problems.

## References
* [OWASP Buffer Overflow Attack]
* [Veracode: What Is a Buffer Overflow? Learn About Buffer Overrun Vulnerabilities, Exploits & Attacks]

[OWASP Buffer Overflow Attack]:https://owasp.org/www-community/attacks/Buffer_overflow_attack
[Veracode: What Is a Buffer Overflow? Learn About Buffer Overrun Vulnerabilities, Exploits & Attacks]:https://www.veracode.com/security/buffer-overflow
