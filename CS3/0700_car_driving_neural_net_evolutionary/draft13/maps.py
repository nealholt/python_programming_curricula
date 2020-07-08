import line_segment

#Create the inner barrier of the race track
hard_track_inner = [(103, 283),(208, 125),(285, 157),(22,305),(339, 372),(513, 400),(657, 256),(746, 145),(801, 292),(699, 363),(728, 488),(563, 472),(47,433),(260, 398),(147, 418)]
#Create the outer barrier of the race track
hard_track_outer = [(21, 237),(202, 35),(396, 85),(36,206),(319, 280),(404, 332),(473, 344),(582, 212),(685, 80),(748, 46),(863, 143),(867, 337),(791, 394),(848, 512),(696, 577),(481, 566),(449, 478),(330, 468),(202, 545),(47, 438),(12, 276)]

medium_track_inner = [(165, 175),(169, 456),(689, 462),(733, 144),(616, 193),(566, 324),(386, 311),(287, 165)]
medium_track_outer = [(2, 4),(4, 595),(896, 594),(895, 1),(575, 8),(523, 135),(330, 129),(238, 6)]

easy_track_inner = [(163, 191),(169, 457),(714, 450),(710, 148)]
easy_track_outer = [(1, 3),(2, 596),(892, 593),(885, 7)]



def getMap(screen, race_track_inner, race_track_outer):
    #The race track is drawn as line segments. Create all the line
    #segments here and add them to the race_track list.
    race_track = []
    white = 255,255,255
    for i in range(len(race_track_inner)-1):
        seg = line_segment.LineSeg(screen, white,
                    race_track_inner[i][0],
                    race_track_inner[i][1],
                    race_track_inner[i+1][0],
                    race_track_inner[i+1][1])
        race_track.append(seg)
    seg = line_segment.LineSeg(screen, white,
                race_track_inner[-1][0],
                race_track_inner[-1][1],
                race_track_inner[0][0],
                race_track_inner[0][1])
    race_track.append(seg)

    for i in range(len(race_track_outer)-1):
        seg = line_segment.LineSeg(screen, white,
                    race_track_outer[i][0],
                    race_track_outer[i][1],
                    race_track_outer[i+1][0],
                    race_track_outer[i+1][1])
        race_track.append(seg)
    seg = line_segment.LineSeg(screen, white,
                race_track_outer[-1][0],
                race_track_outer[-1][1],
                race_track_outer[0][0],
                race_track_outer[0][1])
    race_track.append(seg)
    return race_track

def getMapById(screen, identifier):
    if identifier == 0:
        return getMap(screen, hard_track_inner, hard_track_outer)
    if identifier == 1:
        return getMap(screen, medium_track_inner, medium_track_outer)
    if identifier == 2:
        return getMap(screen, easy_track_inner, easy_track_outer)
