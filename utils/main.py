#!/usr/bin/python3

from google.cloud import translate_v2 as translate
import os
import sys
import six
import pdb

translated_fiels = [
    "generate-core-dump-file.md",
    "set-detach-on-fork.md",
    "print-STL-container.md",
    "set-prompt.md",
    "print-source-lines.md",
    "attach-process.md",
    "modify-pc-register.md",
    "catch-fork.md",
    "option-format.md",
    "select-frame.md",
    "pass-signal.md",
    "break-on-linenum.md",
    "set-read-watchpoint.md",
    "print-formatted-array.md",
    "catch-syscall.md",
    "tui-mode.md",
    "load-executable-and-coredump-file.md",
    "directory.md",
    "break-on-address.md",
    "set-pagination-off.md",
    "set-program-env.md",
    "set-watchpoint.md",
    "set-watchpoint-on-specified-thread.md",
    "disassemble-raw-machine-code.md",
    "catch-ptrace.md",
    "save-breakpoints.md",
    "run-shell-command.md",
    "index.md",
    "keep-unused-types.md",
    "map-source-code-and-assembly.md",
    "print-process-memory.md",
    "print-threads.md",
    "set-tbreak.md",
    "set-condition-break.md",
    "set-var.md",
    "change-string.md",
    "finish-and-return.md",
    "break-on-first-assembly-code.md",
    "print-registers.md",
    "use-short-command.md",
    "print-large-array.md",
    "set-print-pretty-on.md",
    "run-cd-pwd.md",
    "ignore-break.md",
    "layout-asm.md",
    "breakpoint-command.md",
    "send-signal.md",
    "patch-program.md",
    "start-gdb-silently.md",
    "print-array-indexes.md",
    "step-and-next-function.md",
    "examine-memory.md",
    "config-gdbinit.md",
    "substitute-path.md",
    "display-instruction-pc.md",
    "print-ascii-and-wide-string.md",
    "call-func.md",
    "stop-signal.md",
    "info_sharedlibrary.md",
    "print-frame-variables.md",
    "use-$_exitcode.md",
    "set-program-args.md",
    "print-local-variables.md",
    "set-disassembly-flavor.md",
    "catch-vfork.md",
    "tcatch.md",
    "set-script-extension.md",
    "save-history-commands.md",
    "help.md"
    "maint-info-sol-threads.md",
    "quit-gdb-silently.md",
    "use-$_siginfo-variable.md"
      ]


def main():

    translate_client = translate.Client()

    for f in files:
        if f in translated_fiels:
            continue

        translated_fiels.append(f)

        with open(WORKINGDIR + f, "r") as curf:
            text = curf.readlines()
            text = text.decode("utf-8") if  isinstance(text, six.binary_type) else text

        for number, line in enumerate(text):
            for char in line:
                if char > "\u4e00":
                    if len(line) > 100:
                        print()
                        print("line:%d  ->  %s" %(number, line), end="")
                        print()
                    else:
                        print("line:%d  ->  %s" %(number, line), end="")
                    
                    
                    #pdb.set_trace()
                    result = translate_client.translate(line, target_language=target)
                    text[number] = result["translatedText"] + "\n"
                    #print("TRANSLATIONS ->  ", result["translatedText"])
                    break


        with open("done/" + f, "w") as savef:
            text = savef.writelines(text)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("need a path")
        sys.exit(1)


    WORKINGDIR = sys.argv[1]
    files = os.listdir(WORKINGDIR)
    target = "en"

    print("Looking for files in " + WORKINGDIR)
    print()

    main()


