import math

# INPUTS: Raw X, Y positions of each different hand landmark
# OUTPUTS: The distance of each hand landmark from the anchor landmark
# DESC: This function is used to find the total distance between each hand landmark given and 
#       the "anchor" landmark. The anchor landmark is just a landmark on the hand that is used
#       to measure both the distance and angles (next function). We use this hand landmark
#       so we can normalize the position of the hand on the screen. Doing this.
#       no matter where the hand is on the screen the same data will be written. The mathematical
#       function of the distance formula is used to calculate the distances.
def get_hand_distances(hand_positions):
    anchor = hand_positions[0]
    distance_list = []
    for i in range(1, 21): #There are 21 landmarks, but we only need to iterate through 20 since distance between anchor and anchor is 0
        landmark = hand_positions[i]
        distance = math.sqrt((anchor[1] - landmark[1]) ** 2 + (anchor[2] - landmark[2]) ** 2)
        distance = round(distance, 2)
        distance_list.append(distance)
    return distance_list

# INPUTS: Raw X, Y positions of each different hand landmark
# OUTPUTS: The angle of each hand landmark from the anchor landmark
# DESC: This function is used to find the angle between each hand landmark given and 
#       the "anchor" landmark. The anchor landmark is just a landmark on the hand that is used
#       to measure both the distance (prev function) and angles. We use this hand landmark
#       so we can normalize the position of the hand on the screen. Doing this.
#       no matter where the hand is on the screen the same data will be written.
def get_angles(hand_positions):
    anchor = hand_positions[0]
    angles_list = []
    for i in range(1, 21): #There are 21 landmarks, but we only need to iterate through 20 since angle between anchor and anchor is 0
        landmark = hand_positions[i]
        angle = math.atan2((anchor[2] - landmark[2]), (anchor[1] - landmark[1]))
        angle = round(angle, 2)
        angles_list.append(angle)
    return angles_list