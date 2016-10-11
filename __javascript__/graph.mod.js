	(function () {
		var Edge = __class__ ('Edge', [object], {
			get __init__ () {return __get__ (this, function (self, nodes, py_name, avg_distance, direction) {
				self.nodes = (nodes !== null ? nodes : list ([]));
				self.py_name = py_name;
				self.avg_distance = avg_distance;
				self.direction = direction;
			});},
			get message () {return __get__ (this, function (self, a, b) {
				return ((('walk along the ' + str (self.py_name)) + ' to ') + str (b.py_name)) + '.';
			});},
			get __repr__ () {return __get__ (this, function (self) {
				return str (self.nodes);
			});},
			get add_nodes () {return __get__ (this, function (self, nodes) {
				if (type (nodes) !== list) {
					var nodes = list ([nodes]);
				}
				self.nodes += nodes;
			});},
			get dist_between () {return __get__ (this, function (self, a, b) {
				return abs (self.nodes.index (a) - self.nodes.index (b)) * self.avg_distance;
			});},
			get path_sign () {return __get__ (this, function (self, a, b) {
				return (self.nodes.index (a) > self.nodes.index (b) ? 1 : 0);
			});}
		});
		var Node = __class__ ('Node', [object], {
			get __init__ () {return __get__ (this, function (self, py_name, edges) {
				self.py_name = py_name;
				self.edges = edges.__getslice__ (0, null, 1);
			});},
			get add_edge () {return __get__ (this, function (self, edge) {
				self.edges.append (edge);
			});},
			get __repr__ () {return __get__ (this, function (self) {
				return str (self.py_name);
			});}
		});
		var make_edge = function (a, b, edge) {
			if (a !== null) {
				a.edges.append (edge);
				edge.nodes.insert (0, a);
			}
			if (b !== null) {
				b.edges.append (edge);
				edge.nodes.append (b);
			}
		};
		__pragma__ ('<all>')
			__all__.Edge = Edge;
			__all__.Node = Node;
			__all__.make_edge = make_edge;
		__pragma__ ('</all>')
	}) ();
