from os import path, sep
from msvcrt import getch


def wait_for_keypress(prompt: str = "Press any key to exit..."):
    print(prompt, end='', flush=True)
    getch()     # Waits for any key press.


def update_data_path(file_path: str, new_path: str = r"Z:" + sep) -> None:
    """
    Verifica se esiste file_path. Se sì, sostituisce la prima
    (e unica) riga che inizia con "Path_File_Dati=" con new_path.
    """
    if path.isfile(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()

        new_lines = []
        changed = False
        for line in lines:
            if line.startswith("Path_File_Dati="):
                new_lines.append(f"Path_File_Dati={new_path}\n")
                changed = True
                # Aggiunge tutte le righe rimanenti così come sono.
                new_lines.extend(lines[len(new_lines):])
                break
            else:
                new_lines.append(line)

        if changed:
            with open(file_path, "w", encoding="utf-8") as f:
                f.writelines(new_lines)
            print(f"Path updated in: {file_path}")
        else:
            print(f"No lines to modify in {file_path}")
    else:
        print(f"File not found: {file_path}")
        wait_for_keypress()


def main():
    file_path = r"C:" + sep + "Users" + sep + "Public" + sep + "SGA_AZ32.INI"
    new_path = r"Z:" + sep
    
    update_data_path(file_path, new_path)


if __name__ == "__main__":
    main()
