# Source and destination file names.
test_source = "no_inline_delimiters.txt"
test_destination = "no_inline_delimiters.html"

# Keyword parameters passed to publish_file.
reader_name = "standalone"
parser_name = "rst"
writer_name = "html"

# Settings
# test for encoded attribute value:
settings_overrides['no_inline_delimiters'] = True
# local copy of default stylesheet:
settings_overrides['stylesheet_path'] = ( 
            'functional/input/data/html4css1.css')

