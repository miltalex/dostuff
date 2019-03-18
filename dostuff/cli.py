import os, click


@click.group()
def dostuff():
    """
    Simple CLI for automating boring stuff like deleting files.
    """
    pass

@dostuff.command('remove-spaces')
@click.argument('directory', type=click.Path(exists=True))
@click.option(
    '-f', '--file-extension','file_extension', default='.jpg',
    help='File Extension of files to be renamed (e.g. .json)')
def remove_spaces_from_filenames(directory, file_extension):
        """Remove spaces from filenames, corresponding to the given directory and file_extension"""

        for filename in os.listdir(directory):
                if filename.endswith(file_extension):
                        os.rename(os.path.join(directory,filename), 
                                os.path.join(directory,filename.replace(" ", "")))
                        click.secho('File Renamed {}'.format(filename), fg='green')




@dostuff.command('delete-files')
@click.argument('directory', type=click.Path(exists=True))
@click.option(
    '-f', '--file-extension','file_extension', default='.torrent',
    help='File Extension of files to be removed (e.g. .srt)')
def delete_files_with_specific_file_extension(directory, file_extension):
        """Delete files, corresponding to the given directory and file_extension        """

        for filename in os.listdir(directory):
                if filename.endswith(file_extension):
                        click.secho("Removing {}".format(filename), blink=True, bold=True)
                        os.remove('{}/{}'.format(directory, filename))
                        click.secho('File Removed!', fg='green')

                        

        