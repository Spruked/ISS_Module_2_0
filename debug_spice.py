import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from spice_descriptor_layer import SPICEDescriptorLayer
import json

# Just initialize, don't run the demo
layer = SPICEDescriptorLayer()
print('File exists:', layer.descriptor_file.exists())

with open(layer.descriptor_file, 'r') as f:
    lines = f.readlines()
    print('Number of lines:', len(lines))

    for i, line in enumerate(lines[-1:], -len(lines)+1):  # Check last line
        line = line.strip()
        if line:
            print(f'Line {abs(i)}: {line[:50]}...')
            try:
                data = json.loads(line)
                print(f'  Parsed ID: {data.get("descriptor_id")}')
                desc = layer.get_descriptor(data.get('descriptor_id'))
                print(f'  Retrieved: {desc is not None}')
                if desc:
                    print(f'  Descriptor ID: {desc.descriptor_id}')
                    print(f'  Process name: {desc.process_name}')
                else:
                    print('  Trying from_dict directly...')
                    from spice_descriptor_layer import SPICEDescriptor
                    desc2 = SPICEDescriptor.from_dict(data)
                    print(f'  from_dict worked: {desc2.descriptor_id}')
            except Exception as e:
                print(f'  Error: {e}')
                import traceback
                traceback.print_exc()