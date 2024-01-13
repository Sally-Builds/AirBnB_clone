#!/usr/bin/python3

"""Console interpreter"""
import cmd

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def emptyline(self):
        """ do nothing the interpreter"""
        pass

    def help_quit(self):
        """ quit helper description"""
        print("Quit command to exit the program")

    def do_quit(self, arg):
        """quit the program"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
