def build_expression_graph(leaves, operations):
    nodes = {}                                # id -> record
    records = []

    for leaf in leaves:
        rec = {
            "id": leaf["id"],
            "data": leaf["data"],
            "grad": 0.0,
            "op": "",
            "parents": [],
        }
        nodes[rec["id"]] = rec
        records.append(rec)

    for op_rec in operations:
        x = nodes[op_rec["left"]]["data"]
        y = nodes[op_rec["right"]]["data"]
        z = x + y if op_rec["op"] == "+" else x * y
        rec = {
            "id": op_rec["id"],
            "data": z,
            "grad": 0.0,
            "op": op_rec["op"],
            "parents": [op_rec["left"], op_rec["right"]],
        }
        nodes[rec["id"]] = rec
        records.append(rec)

    final_id = operations[-1]["id"] if operations else leaves[-1]["id"]
    return records, final_id