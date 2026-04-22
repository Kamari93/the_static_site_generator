def markdown_to_blocks(markdown):
   blocks = [block.strip() for block in markdown.split("\n\n") if block.strip()]
    
   return blocks


    # return_list = []
    # for block in markdown.split("\n\n"):
    #     if block.strip():
    #         return_list.append(block.strip())

    # return return_list