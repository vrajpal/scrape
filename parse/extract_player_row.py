from parse import create_player_row as create_player_stats

def get_player_row(rows):
    for row in rows:
        # find the data cell with player in it
        breakpoint()
        position_row = row.find("td", {"data-stat": "pos"})
        if position_row is not None:
            position = position_row.contents[0].text
            # if the player is not a pitcher, process it
            if position !=  "P" and position is not None:
                # print("Position: ")
                # print(position)
                create_player_stats(row)