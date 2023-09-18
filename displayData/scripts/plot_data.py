import base64
import io
from matplotlib import pyplot as plt
from displayData.scripts.read_data import get_data_frame


def plot_data_with_bar(input_data_file, x_axis_name, y_axis_name):
    raw_data = get_data_frame(input_data_file)
    plt.figure(figsize=(12, 6))
    plt.bar(raw_data[x_axis_name], raw_data[y_axis_name])
    image_file = io.BytesIO()
    plt.savefig(image_file)
    b64_raw_image_data = base64.b64encode(image_file.getvalue()).decode()
    return b64_raw_image_data
