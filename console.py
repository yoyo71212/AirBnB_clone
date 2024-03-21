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
                try:
                    if args[3].isdigit():
                        args[3] = int(args[3])
                    elif args[3].replace('.', '', 1).isdigit():
                        args[3] = float(args[3])
                    else:
                        args[3] = args[3].replace('"', '').replace("'", '')
                except AttributeError:
                    pass
                setattr(instance, args[2], args[3])
                models.storage.save()
        return

    def count(self, arg):
        args = arg.split()
        args_len = len(args)
        if args_len == 1:
            if args[0] not in self.class_opts:
                print('** class doesn\'t exist **')
            else:
                res = 0
                stored = models.storage.all()
                for k in stored:
                    if k.split('.')[0] == args[0]:
                        res += 1
                print(res)
        return

    def default(self, arg):
        args = arg.split('.', 1)
        if args[0] in self.class_opts:
            if args[1].strip('()') == 'all':
                self.do_all(args[0])
            elif args[1].strip('()') == 'count':
                self.count(args[0])
            elif args[1].split('(')[0] == 'show':
                inst_id = args[1].split('(')[1].strip(')') \
                            .replace('"', '').replace("'", '')
                self.do_show(args[0] + ' ' + inst_id)
            elif args[1].split('(')[0] == 'destroy':
                inst_id = args[1].split('(')[1].strip(')') \
                            .replace('"', '').replace("'", '')
                self.do_destroy(args[0] + ' ' + inst_id)
            elif args[1].split('(')[0] == 'update':
                inst = args[1].split('(')[1].strip(')')
                if '{' in inst:
                    inst_len = len(inst.split(', ', 1))
                else:
                    inst_len = len(inst.split(', '))
                if inst_len == 3:
                    inst = inst.replace(',', '').replace('"', '') \
                            .replace("'", '')
                    self.do_update(args[0] + ' ' + inst)
                elif inst_len == 2:
                    temp = inst.split(', ', 1)
                    temp_dict = eval(temp[1])
                    for k, v in temp_dict.items():
                        inst = args[0] + ' ' + temp[0] + ' ' + \
                                str(k) + ' ' + str(v)
                        self.do_update(inst)
            else:
                print('*** Unknown syntax: ' + arg)
        elif len(args) == 2:
            print('** class doesn\'t exist **')
        else:
            print('*** Unkown syntax: ' + arg)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
