#!/usr/bin/env python
# pylint: disable=C0103,C0303
import paragraph


class Application():
    @classmethod
    def main(cls, filename: str) -> None:
        """The main function of Application class is to print out the result on screen 
    
        Args:
            filename(str): input file
        
        Returns:
            None
            
        """
        pgh = paragraph.Paragraph()
        pgh.read(filename)
        pgh.output()


if __name__ == "__main__":
    # I think it's more interestring if player can get input from standard input and reponse answer interactively
    input_filename = '../input_file.txt'
    Application.main(input_filename)
