def copy_file(command: str) -> None:
    comand_list = command.split()

    if len(comand_list) != 3:
        return

    if comand_list[0] == "cp":
        if comand_list[1] != comand_list[2]:
            try:
                with open(comand_list[1], "r") as file_in, \
                     open(comand_list[2], "w") as file_out:
                    need_to_write = file_in.read()
                    file_out.write(need_to_write)
            except FileNotFoundError:
                pass
