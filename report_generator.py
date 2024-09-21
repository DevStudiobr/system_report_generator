import psutil
import json
from rich.console import Console
from rich.prompt import Prompt

console = Console()

def gather_system_info():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage('/')

    return {
        "cpu_usage": cpu_usage,
        "memory_usage": {
            "total": memory.total,
            "used": memory.used,
            "percent": memory.percent
        },
        "disk_usage": {
            "total": disk.total,
            "used": disk.used,
            "percent": disk.percent
        }
    }

def generate_report(info, format='text'):
    if format == 'json':
        return json.dumps(info, indent=4)
    else:
        report = (
            f"Uso da CPU: {info['cpu_usage']}%\n"
            f"Uso de Memória: {info['memory_usage']['percent']}% "
            f"(Usado: {info['memory_usage']['used'] / (1024 ** 2):.2f} MB, Total: {info['memory_usage']['total'] / (1024 ** 2):.2f} MB)\n"
            f"Uso de Disco: {info['disk_usage']['percent']}% "
            f"(Usado: {info['disk_usage']['used'] / (1024 ** 3):.2f} GB, Total: {info['disk_usage']['total'] / (1024 ** 3):.2f} GB)\n"
        )
        return report

def main():
    console.print("[bold cyan]Gerador de Relatórios do Sistema[/bold cyan]")
    format_choice = Prompt.ask("Escolha o formato do relatório (texto/json)", choices=["texto", "json"])
    info = gather_system_info()
    report = generate_report(info, format='json' if format_choice == 'json' else 'text')
    
    console.print("\n[bold blue]Relatório:[/bold blue]")
    console.print(report)

if __name__ == "__main__":
    main()
