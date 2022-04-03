"""
This file is intended to be used to generate settings JSON files for QMENTA.
"""

import argparse
import json


def parse_arguments():
    parser = argparse.ArgumentParser(description='Generate QMENTA settings JSON files')

    parser.add_argument('--file_name', nargs="?", default="QMENTA_settings.json", help='Name of the settings file, including directory. Overwrites existing files')
    parser.add_argument('--heading', nargs="?", default="", help='Heading for the settings')
    parser.add_argument('--num_objects', help='Number of objects in the settings. These objects will usually be inputs')

    # the  information that the user wants to define about each object
    parser.add_argument("--obj_type", nargs="*", default=None, help="For each object, you must specify the \"type\" value in a list.")
    parser.add_argument("--obj_id", nargs="*", default=None, help="For each object, you must specify the \"id\" value in a list.")
    parser.add_argument("--obj_title", nargs="*", default=None, help="For each object, specify \"title\". If any input has a \"title\" value, you must specify a value for them all, even if it is \"None\"")
    parser.add_argument("--obj_file_filter", nargs="*", default=None, help="For each object, specify \"file_filter\". If any input has a \"file_filter\" value, you must specify a value for them all, even if it is \"None\"")
    parser.add_argument("--obj_in_filter", nargs="*", default=None, help="For each object, specify \"in_filter\". If any input has a \"in_filter\" value, you must specify a value for them all, even if it is \"None\"")
    parser.add_argument("--obj_out_filter", nargs="*", default=None, help="For each object, specify \"out_filter\". If any input has a \"out_filter\" value, you must specify a value for them all, even if it is \"None\"")
    parser.add_argument("--obj_anchor", nargs="*", default=None, help="For each object, specify \"anchor\". If any input has a \"anchor\" value, you must specify a value for them all, even if it is \"None\"")
    parser.add_argument("--obj_mandatory", nargs="*", default=None, help="For each object, specify \"mandatory\". If any input has a \"mandatory\" value, you must specify a value for them all, even if it is \"None\"")
    parser.add_argument("--obj_batch", nargs="*", default=None, help="For each object, specify \"batch\". If any input has a \"batch\" value, you must specify a value for them all, even if it is \"None\"")
    parser.add_argument("--obj_min", nargs="*", default=None, help="For each object, specify \"min\". If any input has a \"min\" value, yyou must specify a value for them all, even if it is \"None\"")
    parser.add_argument("--obj_max", nargs="*", default=None, help="For each object, specify \"max\". If any input has a \"max\" value, you must specify a value for them all, even if it is \"None\"")

    args = parser.parse_args()
    return args


"""
Construct an object to put in the JSON file
"""
def construct_object(obj_type=None, obj_id=None, obj_title=None, obj_file_filter=None, obj_in_filter=None,
                     obj_out_filter=None, obj_anchor=None, obj_mandatory=None, obj_batch=None, obj_min=None,
                     obj_max=None):
    generated_object = {}

    if obj_type is None:
        print("obj_type missing, failed to create object")
        return
    else:
        generated_object["type"] = obj_type

    if obj_id is None:
        print("obj_id missing, failed to create object")
        return
    else:
        generated_object["id"] = obj_id

    if obj_title is None:
        print("obj_title missing, failed to create object")
        return
    else:
        generated_object["title"] = obj_title

    if obj_file_filter is None:
        print("obj_file_filter missing, failed to create object")
        return
    else:
        generated_object["file_filter"] = obj_file_filter

    if obj_in_filter is None:
        print("obj_in_filter missing, failed to create object")
        return
    else:
        generated_object["in_filter"] = obj_in_filter

    if obj_out_filter is None:
        print("obj_out_filter missing, failed to create object")
        return
    else:
        generated_object["out_filter"] = obj_out_filter

    if obj_anchor is None:
        print("obj_anchor missing, failed to create object")
        return
    else:
        generated_object["anchor"] = obj_anchor

    if obj_mandatory is None:
        print("obj_mandatory missing, failed to create object")
        return
    else:
        generated_object["mandatory"] = obj_mandatory

    if obj_batch is None:
        print("obj_batch missing, failed to create object")
        return
    else:
        generated_object["batch"] = obj_batch

    if obj_min is None:
        print("obj_min missing, failed to create object")
        return
    else:
        generated_object["min"] = obj_min

    if obj_max is None:
        print("obj_max missing, failed to create object")
        return
    else:
        generated_object["max"] = obj_max

    return generated_object


def main():
    """
    Generate the settings file
    """
    args = parse_arguments()

    settings = []


    heading = {
        "type": "heading",
        "content": args.heading
    }
    settings.append(heading)

    for i in range(int(args.num_objects)):
        obj_type = args.obj_type[i]
        obj_id = args.obj_id[i]
        title = args.obj_title[i]
        file_filter = args.obj_file_filter[i]
        in_filter = args.obj_in_filter[i]
        out_filter = args.obj_out_filter[i]
        anchor = args.obj_anchor[i]
        mandatory = args.obj_mandatory[i]
        batch = args.obj_batch[i]
        obj_min = args.obj_min[i]
        obj_max = args.obj_max[i]
        settings.append(construct_object(obj_type, obj_id, title, file_filter, in_filter, out_filter, anchor, mandatory, batch, obj_min, obj_max))

    # write json output to file
    file = open(args.file_name, "w")
    file.write(json.dumps(settings, indent=4))
    file.close()

    # for debugging
    file = open(args.file_name, "r")
    print(file.read())
    file.close()


if __name__ == "__main__":
    main()
