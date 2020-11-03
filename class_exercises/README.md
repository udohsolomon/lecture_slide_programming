# Buffer Overflow

## Description
Buffer overflows are probably one of the most vicious tools available to an attacker. A small honest mistake made by a developer with SETUID root permissions can mean catastrophe. 

A buffer overflow is the technique of overwriting machine code with an attackers own code, this occurs when a program takes input from a user in low-level languages such as c, c++ without checking its size. It can be used to gain root access.

To effectively mitigate buffer overflow vulnerabilities, it is important to understand what buffer overflows are, what dangers they pose to your applications, and what techniques attackers use to successfully exploit these vulnerabilities.

## Vulnerabilities

### gets()
The stdio gets() function does not check for buffer length and always results in a vulnerability.

```
#include <signal.h>
#include <stdio.h>
#include <string.h>
int main () {
    char username[8];
    int allow = 0;
    printf external link("Enter your username, please: ");
    gets(username); // user inputs "malicious"
    if (grantAccess(username)) {
        allow = 1;
    }
    if (allow != 0) { // has been overwritten by the overflow of the username.
        privilegedAction();
    }
    return 0;
}
```
## Mitigation
Prefer using fgets (and dynamically allocated memory!):
```c
#include <stdio.h>
#include <stdlib.h>
#define LENGTH 8
int main () {
    char* username, *nlptr;
    int allow = 0;
 
    username = malloc(LENGTH * sizeof(*username));
    if (!username)
        return EXIT_FAILURE;
    printf external link("Enter your username, please: ");
    fgets(username,LENGTH, stdin);
    // fgets stops after LENGTH-1 characters or at a newline character, which ever comes first.
    // but it considers \n a valid character, so you might want to remove it:
    nlptr = strchr(username, '\n');
    if (nlptr) *nlptr = '\0';
 
    if (grantAccess(username)) {
        allow = 1;
    }
    if (allow != 0) {
        priviledgedAction();
    }
 
    free(username);
 
    return 0;
}
```

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
