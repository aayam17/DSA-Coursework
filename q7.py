import tkinter as tk
from tkinter import ttk, messagebox
import networkx as nx
import matplotlib.pyplot as plt

class RouteOptimizationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Route Optimization for Delivery Service")

        # Initialize sample graph
        self.G = self.create_sample_graph()

        # Create GUI components
        self.create_widgets()

    def create_sample_graph(self):
        G = nx.Graph()
        # Adding cities and weighted edges (distances)
        G.add_weighted_edges_from([
            ("CityA", "CityB", 10),
            ("CityA", "CityC", 15),
            ("CityA", "CityD", 20),
            ("CityB", "CityC", 35),
            ("CityB", "CityD", 25),
            ("CityC", "CityD", 30),
            ("CityD", "CityE", 20),
            ("CityE", "CityF", 10),
            ("CityF", "CityG", 15),
            ("CityG", "CityH", 25),
            ("CityH", "CityA", 30),
            ("CityH", "CityE", 5)
        ])
        return G

    def create_widgets(self):
        # Delivery List Section
        tk.Label(self.root, text="Delivery Points (comma-separated addresses):").pack(pady=5)
        self.delivery_entry = tk.Entry(self.root, width=50)
        self.delivery_entry.pack(pady=5)

        # Vehicle Options Section
        tk.Label(self.root, text="Vehicle Capacity:").pack(pady=5)
        self.capacity_entry = tk.Entry(self.root, width=20)
        self.capacity_entry.pack(pady=5)

        tk.Label(self.root, text="Driving Distance Constraint:").pack(pady=5)
        self.distance_entry = tk.Entry(self.root, width=20)
        self.distance_entry.pack(pady=5)

        # Algorithm Selection
        tk.Label(self.root, text="Select Algorithm:").pack(pady=5)
        self.algorithm_combo = ttk.Combobox(self.root, values=["Nearest Neighbor"])
        self.algorithm_combo.pack(pady=5)
        self.algorithm_combo.set("Nearest Neighbor")

        # Optimize Button
        tk.Button(self.root, text="Optimize Route", command=self.optimize_route).pack(pady=5)

        # Result Area
        self.result_area = tk.Text(self.root, height=10, width=60)
        self.result_area.pack(pady=5)

    def optimize_route(self):
        delivery_points = self.delivery_entry.get().split(',')
        capacity = int(self.capacity_entry.get())
        distance_constraint = float(self.distance_entry.get())

        if not delivery_points:
            messagebox.showerror("Input Error", "Please enter delivery points.")
            return

        delivery_points = [point.strip().lower() for point in delivery_points]

        if len(delivery_points) < 2:
            messagebox.showerror("Input Error", "At least two delivery points are required.")
            return

        try:
            algorithm = self.algorithm_combo.get()
            if algorithm == "Nearest Neighbor":
                path = self.nearest_neighbor_tsp(delivery_points)
                self.result_area.delete(1.0, tk.END)
                self.result_area.insert(tk.END, f"Optimal Path: {path}\n")
                self.visualize_route(path)
            else:
                messagebox.showerror("Algorithm Error", "Selected algorithm is not implemented.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def nearest_neighbor_tsp(self, nodes):
        start = nodes[0]
        path = [start]
        unvisited = set(nodes)
        unvisited.remove(start)

        current = start
        while unvisited:
            next_node = min(unvisited, key=lambda node: self.G.get_edge_data(current, node, {}).get('weight', float('inf')))
            path.append(next_node)
            unvisited.remove(next_node)
            current = next_node

        path.append(start)  # Return to start
        return path

    def visualize_route(self, path):
        plt.clf()
        pos = nx.spring_layout(self.G)
        nx.draw(self.G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=500, font_size=16)

        path_edges = list(zip(path, path[1:]))
        nx.draw_networkx_nodes(self.G, pos, nodelist=path, node_color='lightgreen')
        nx.draw_networkx_edges(self.G, pos, edgelist=path_edges, edge_color='red', width=2)

        plt.title("Route Visualization")
        plt.show()

def main():
    root = tk.Tk()
    app = RouteOptimizationApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
