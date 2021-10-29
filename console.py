#!/usr/bin/python3
'''Console module'''
import cmd
import models
import readline


class HBNBCommand(cmd.Cmd):
    '''Console class for builtin commands'''

    prompt = '(hbnb) '

    def do_quit(self, args):
        '''quit:
        Exits the application
        '''
        raise SystemExit

    def do_EOF(self, args):
        '''EOF:
        Exits application on End of File
        '''
        raise SystemExit

    def emptyline(self):
        '''Handles emptyline'''
        pass

    def do_create(self, args):
        '''create:
        Creates a BaseModel object, Saves it to JSON file, and Prints the id
        '''
        if not args:
            return print('** class name missing **')

        try:
            thing = getattr(models, args)()
            models.storage.new(thing)
            models.storage.save()
            print(thing.id)
        except Exception:
            print("** class doesn't exist **")

    def do_show(self, args):
        '''show:
        Print the __str__ of an object by class & id
        '''
        if not args:
            return print('** class name missing **')

        try:
            getattr(models, args.split(' ')[0])
        except Exception:
            return print("** class doesn't exist **")

        if len(args.split(' ')) < 2:
            return print('** instance id missing **')

        try:
            print(str(
                models.storage.all()['.'.join(i for i in args.split(' '))]))
        except Exception:
            print('** no instance found **')

    def do_destroy(self, args):
        '''destoy:
        Delete an instance of an object by class & id
        '''
        if not args:
            return print('** class name missing **')

        try:
            getattr(models, args.split(' ')[0])
        except Exception:
            return print("** class doesn't exist **")

        if len(args.split(' ')) < 2:
            return print('** instance id missing **')

        try:
            del models.storage.all()['.'.join(i for i in args.split(' '))]
            models.storage.save()
        except Exception:
            print('** no instance found **')

    def do_all(self, args):
        '''all:
        Print a list of all active objects in storage.
        '''
        if args:
            try:
                getattr(models, args.split(' ')[0])
                print([str(models.storage.all()[key])
                      for key in models.storage.all() if key.split('.')[0] == args])
            except Exception:
                return print("** class doesn't exist **")
        else:
            print([str(models.storage.all()[key])
                  for key in models.storage.all()])

    def do_update(self, args):
        '''update:
        Update the attribute value of an active object in storage
        '''
        if not args:
            return print('** class name missing **')

        argz = args.split(' ')

        try:
            getattr(models, argz[0])
        except Exception:
            return print("** class doesn't exist **")

        if len(argz) < 2:
            return print('** instance id missing **')

        try:
            models.storage.all()[argz[0] + '.' + argz[1]]
        except Exception:
            return print('** no instance found **')

        if len(argz) < 3:
            return print('** attribute name missing **')

        if len(argz) < 4:
            return print('** value missing **')

        try:
            setattr(
                models.storage.all()[argz[0] + '.' + argz[1]],
                argz[2],
                argz[3].strip('"')
            )
            models.storage.save()
        except Exception:
            print('** no instance found **')


if __name__ == '__main__':
    HBNBCommand().cmdloop()
