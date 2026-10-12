# ini hanya project have fun untuk portofolio pribadi
# docstring, function, return

#pertama initisalisasi variable awal

expected_time = 40
preparation_time = 2

def bake_time_remaining(elapsed_bake_time):

    """Calculate the bake time remaining.

    Parameters:
  
        elapsed_bake_time (int): The baking time already elapsed.

    Returns:

        int: The remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.      
    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    return expected_time - elapsed_bake_time

def preparation_time_in_minutes(number_of_layers):

    """di sini kita menghitung waktu persiapan di kali/multiply dengan number_of_layers/jumlah layer"""

    return number_of_layers * preparation_time

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):

    """di sini kita menghitung waktu yang tersisa dari memanggang lasagna dengan 
    menambah/addition fungsi preparation_time_in_minutes di addition dengan elapsed_bake_time"""

    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time  

        