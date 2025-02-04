if len(sys.argv)>3:
    sys.exit("Too many command-line arguments")
elif len(sys.argv)<3:
    sys.exit("Too few command-line arguments")
else:
    file,ext = os.path.splitext(sys.argv[])

