from ai_edge_quantizer.utils import tfl_flatbuffer_utils

input_model = "C:\\Users\\Admin\\Documents\\Projects\\yolov26-pokemon\\web\\public\\baybayin-main\\best_int8.tflite"  # or "best_int8.tflite"
output_model = "model_fixed.tflite"

# Resolves external offset buffers back into inline .data buffers
print("Reading model...")
model = tfl_flatbuffer_utils.read_model(input_model)

print("Writing model with inline buffers...")
tfl_flatbuffer_utils.write_model(model, output_model)

print(f"Done! Use '{output_model}' in your HTML page.")