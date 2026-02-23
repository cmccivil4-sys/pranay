class CircuitVisionPipeline:
    async def scan(self, image_name: str) -> dict:
        return {
            'detected_components': ['R1', 'C1', 'V1'],
            'netlist': 'V1 n1 0 DC 5; R1 n1 n2 1k; C1 n2 0 10u',
            'simulation': {'voltage_n2': '3.1V', 'status': 'stable'},
            'errors': [],
            'source_image': image_name,
        }


cv_pipeline = CircuitVisionPipeline()
