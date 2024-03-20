#!/usr/bin/python3
''' Entry point of the command interpreter '''

import cmd
import sys
import models
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):

    prompt = '(hbnb) '
    class_opts = {
            'BaseModel', 'User', 'Place', 'State', 'City', 'Amenity', 'Review'
            }

    def do_quit(self, arg):
        ''' quit to exit the program '''
        return True

    def do_EOF(self, arg):
        ''' EOF to exit the program '''
        return True

    def emptyline(self):
        ''' an empty line + ENTER shouldn’t execute anything '''
        pass

    def do_create(self, arg):
        '''
        Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id
        '''
        if arg:
            try:
                cls = getattr(sys.modules[__name__], arg)
                instance = cls()
                print(instance.id)
                models.storage.save()
            except AttributeError:
                print('** class doesn\'t exist **')
        else:
            print('** class name missing **')
        return

    def do_show(self, arg):
        '''
        Prints the string representation of an instance
        based on the class name and id
        '''
        args = arg.split()
        args_len = len(args)
        if args_len == 0:
            print('** class name missing **')
        elif args_len == 1:
            print('** instance id missing **')
        elif args[0] not in self.class_opts:
            print('** class doesn\'t exist **')
        else:
            stored = models.storage.all()
            k = args[0] + '.' + args[1]
            if k in stored:
                print(stored[k])
            else:
                print('** no instance found **')
        return

    def do_destroy(self, arg):
        '''
        Deletes an instance based on the class name and id
        (save the change into the JSON file)
        '''
        args = arg.split()
        args_len = len(args)
        if args_len == 0:
            print('** class name missing **')
        elif args_len == 1:
            print('** instance id missing **')
        elif args[0] not in self.class_opts:
            print('** class doesn\'t exist **')
        else:
            stored = models.storage.all()
            k = args[0] + '.' + args[1]
            if k in stored:
                del stored[k]
                models.storage.save()
            else:
                print('** no instance found **')
        return

    def do_all(self, arg):
        '''
        Prints all string representation of
        all instances based or not on the class name
        '''
        res = []
        args = arg.split()
        args_len = len(args)
        stored = models.storage.all()
        if args_len == 0:
            for k in stored:
                res.append(str(stored[k]))
        elif args[0] not in self.class_opts:
            print('** class doesn\'t exist **')
        else:
            for k in stored:
                if k.split('.')[0] == args[0]:
                    res.append(str(stored[k]))
        if res:
            print(res)
        return

    def do_update(self, arg):
        '''
        Updates an instance based on the class name and id
        by adding or updating attribute (save the change into the JSON file)
        '''
        args = arg.split()
        args_len = len(args)
        if args_len == 0:
            print('** class name missing **')
        elif args_len == 1:
            print('** instance id missing **')
        elif args_len == 2:
            print('** attribute name missing **')
        elif args_len == 3:
            print('** value missing **')
        elif args[0] not in self.class_opts:
            print('** class doesn\'t exist **')
        else:
            stored = models.storage.all()
            k = args[0] + '.' + args[1]
            if not stored[k]:
                print('** no instance found **')
            else:
                instance = stored[k]
                setattr(instance, args[2], args[3])
                models.storage.save()
        return


if __name__ == '__main__':
    HBNBCommand().cmdloop()
