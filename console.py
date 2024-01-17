#!/usr/bin/python3

"""Console interpreter"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Command Line Interpreter"""
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

    def do_create(self, arg):
        """create object"""
        from models.base_model import BaseModel
        if arg == "":
            print("** class name missing **")
        elif arg == BaseModel.__name__:
            obj = BaseModel()
            print(obj.id)
        else:
            print("** class doesn't exist **")
    
    def do_show(self, args):
        """ Show string representation of instance object"""
        from models.base_model import BaseModel
        from models import storage
        values = args.split(" ")
        if args == "":
            print("** class name missing **")
        elif values[0] != BaseModel.__name__:
            print("** class doesn't exist **")
        elif len(values) < 2:
            print("** instance id missing **")
        elif len(values) > 2:
            print("** no instance found **")
        else:
            objects = storage.all()
            val = BaseModel.__name__ + "." + values[1]
            if val in objects:
                print(str(objects[val]))
            else:
                print("** no instance found **")

    def do_destroy(self, args):
        """Delete instance from storage"""
        from models.base_model import BaseModel
        from models import storage
        values = args.split(" ")
        if args == "":
            print("** class name missing **")
        elif values[0] != BaseModel.__name__:
            print("** class doesn't exist **")
        elif len(values) < 2:
            print("** instance id missing **")
        elif len(values) > 2:
            print("** no instance found **")
        else:
            objects = storage.all()
            val = BaseModel.__name__ + "." + values[1]
            if val in objects:
                del objects[val]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, args):
        """returns list of all instances saved""" 
        from models.base_model import BaseModel
        from models import storage
        if args == "" or args == BaseModel.__name__:
            obj_list = []
            objects = storage.all()
            
            for key in objects:
                obj_list.append(str(objects[key]))

            print(obj_list)


    def do_update(self, args):
        """updates instance attribute"""
        from models.base_model import BaseModel
        from models import storage
        values = args.split(" ")

        if args == "":
            print("** class name missing **")
        
        elif values[0] != BaseModel.__name__:
            print("** class doesn't exist **")

        elif len(values) <= 1:
            print("** instance id missing **")
        else:
            objects = storage.all()
            _id = BaseModel.__name__ + "." + values[1]
            if _id in objects:
                if len(values) <= 2:
                    print("** attribute name missing **")
                elif len(values) <= 3:
                    print("** value missing **")
                else:
                    obj = objects[_id]
                    obj.__dict__[values[2]] = values[3].strip('"')
                    storage.save()
            else:
                print("** no instance found **")







if __name__ == '__main__':
    HBNBCommand().cmdloop()
