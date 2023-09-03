import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.backends.backend_pdf as pdf


def pdf_generate(output_file, title):
    rc = {'font.sans-serif': 'Arial Unicode MS'}
 
    df = pd.read_csv(f'{output_file}.csv')

    df_ers_konto = df[df['Art'] == '退款'].groupby('Konto')['Betrag'].sum().reset_index()
    df_ers_kat = df[df['Art'] == '退款'].groupby('Kategorie')['Betrag'].sum().reset_index()
    df_ers_bes = df[df['Art'] == '退款'].groupby(['Kategorie', 'Beschreibung'])['Betrag'].sum().reset_index()

    df_aus_konto_a = df[df['Art'] == '支出'].groupby('Konto')['Betrag'].sum().reset_index()
    df_aus_konto = df_aus_konto_a.merge(df_ers_konto, on='Konto', how='left').fillna(0)
    df_aus_konto = df_aus_konto.rename(columns={'Betrag_x': 'Betrag', 'Betrag_y': '退款'})
    df_aus_konto['Betrag_sum'] = df_aus_konto['Betrag'] - df_aus_konto['退款']
    df_aus_konto_sorted = df_aus_konto.sort_values('Betrag_sum', ascending=False)

    df_aus_kat_a = df[df['Art'] == '支出'].groupby('Kategorie')['Betrag'].sum().reset_index()
    df_aus_kat = df_aus_kat_a.merge(df_ers_kat, on='Kategorie', how='left').fillna(0)
    df_aus_kat = df_aus_kat.rename(columns={'Betrag_x': 'Betrag', 'Betrag_y': '退款'})
    df_aus_kat['Betrag_sum'] = df_aus_kat['Betrag'] - df_aus_kat['退款']
    df_aus_kat_sorted = df_aus_kat.sort_values('Betrag_sum', ascending=False)

    df_aus_bes_a = df[df['Art'] == '支出'].groupby(['Kategorie', 'Beschreibung'])['Betrag'].sum().reset_index()
    df_aus_bes = df_aus_bes_a.merge(df_ers_bes, on=['Kategorie', 'Beschreibung'], how='left').fillna(0)
    df_aus_bes = df_aus_bes.rename(columns={'Betrag_x': 'Betrag', 'Betrag_y': '退款'})
    df_aus_bes['Betrag_sum'] = df_aus_bes['Betrag'] - df_aus_bes['退款']
    df_aus_bes_sorted = df_aus_bes.sort_values('Betrag_sum', ascending=False)

    def aus_konto(df):
        plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
        sns.set(style="white", palette=["#d3ba68", "#6E3F2B", "#B3686F", "#41553A",
                                            "#E7BB7C", "#AA4414", "#EBA54C", "#214866",
                                            "#3D4D29", "#6F5379", "#9cada1", "#8398af",
                                            "#dfabb9", "#c7c7bb", "#9f7a62", "#b3acc7",
                                            "#7e716f", "#d3b9b9"], rc=rc)
        plt.figure(figsize=(8, 4), facecolor="#eee1ca")
        ax = sns.barplot(data=df, y='Konto', x='Betrag_sum', linewidth=0)
        ax.set_facecolor("#eee1ca")
        plt.title('账户', ha='center', va='center', fontsize=16, fontweight='bold')
        plt.xlabel(None)
        plt.ylabel(None)
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['left'].set_visible(False)
        ax.spines['bottom'].set_visible(False)
        max_width = ax.get_xlim()[1]
        offset = max_width/40
        for p in ax.patches:
            width = p.get_width()
            plt.text(width + offset, p.get_y() + p.get_height() / 2, f'{width:.2f}', ha='left', va='center', fontweight='bold')
        total_betrag = df['Betrag_sum'].sum()
        plt.text(0.98, 0.02, f'总支出: {total_betrag:.2f}', transform=plt.gca().transAxes,
                ha='right', va='bottom', fontweight='bold')
        plt.gca().xaxis.grid(False)
        plt.xticks([])
        plt.gca().yaxis.grid(False) 
        plt.tight_layout()
        return plt

    def aus_kat(df):
        plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
        sns.set(style="whitegrid", palette=["#d3ba68", "#6E3F2B", "#B3686F", "#41553A",
                                            "#E7BB7C", "#AA4414", "#EBA54C", "#214866",
                                            "#3D4D29", "#6F5379", "#9cada1", "#8398af",
                                            "#dfabb9", "#c7c7bb", "#9f7a62", "#b3acc7",
                                            "#7e716f", "#d3b9b9"],rc=rc)
        plt.figure(figsize=(8, 4), facecolor="#eee1ca")
        ax = sns.barplot(data=df, y='Kategorie', x='Betrag_sum', linewidth=0)
        ax.set_facecolor("#eee1ca")
        plt.title('类别', ha='center', va='center', fontsize=16, fontweight='bold')
        plt.xlabel(None)
        plt.ylabel(None)
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['left'].set_visible(False)
        ax.spines['bottom'].set_visible(False)
        plt.gca().xaxis.grid(False)
        plt.xticks([])
        plt.gca().yaxis.grid(False)
        max_width = ax.get_xlim()[1]
        offset = max_width/40
        for p in ax.patches:
            width = p.get_width()
            plt.text(width + offset, p.get_y() + p.get_height() / 2, f'{width:.2f}', ha='left', va='center', fontweight='bold')
        plt.tight_layout()
        return plt

    def aus_kat_bes(df):
        plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
        sns.set(style="whitegrid", palette=["#d3ba68", "#6E3F2B", "#B3686F", "#41553A",
                                            "#E7BB7C", "#AA4414", "#EBA54C", "#214866",
                                            "#3D4D29", "#6F5379", "#9cada1", "#8398af",
                                            "#dfabb9", "#c7c7bb", "#9f7a62", "#b3acc7",
                                            "#7e716f", "#d3b9b9"],rc=rc)
        for category_name, group in df.groupby('Kategorie'):
            plt.figure(figsize=(8, 4), facecolor="#eee1ca")
            ax = sns.barplot(data=group, y='Beschreibung', x='Betrag_sum', linewidth=0)
            ax.set_facecolor("#eee1ca")
            plt.title(f'{category_name}', ha='center', va='center', fontsize=16, fontweight='bold')
            plt.xlabel(None)
            plt.ylabel(None)
            ax.spines['top'].set_visible(False)
            ax.spines['right'].set_visible(False)
            ax.spines['left'].set_visible(False)
            ax.spines['bottom'].set_visible(False)
            plt.gca().xaxis.grid(False)
            plt.xticks([])
            plt.gca().yaxis.grid(False)
            max_width = ax.get_xlim()[1]
            offset = max_width/40
            for p in ax.patches:
                width = p.get_width()
                plt.text(width + offset, p.get_y() + p.get_height() / 2, f'{width:.2f}', ha='left', va='center', fontweight='bold')
            plt.tight_layout()
            yield plt

    with pdf.PdfPages(f'{output_file}.pdf') as pdf_output:
        plt_title = plt.figure(figsize=(8, 4), facecolor="#eee1ca")
        plt_title.text(0.5, 0.5, title, ha='center', va='center', fontsize=20, fontweight='bold')
        pdf_output.savefig(plt_title)
        plt.close(plt_title)

        plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
        ausgaben = plt.figure(figsize=(8, 4), facecolor="#eee1ca")
        ausgaben.text(0.5, 0.5, '支出', ha='center', va='center', fontsize=21, fontweight='bold')
        pdf_output.savefig(ausgaben)
        plt.close(ausgaben)

        plt_aus_konto = aus_konto(df_aus_konto_sorted)
        plt_aus_konto.tight_layout()
        pdf_output.savefig(plt_aus_konto.gcf())
        plt_aus_konto.close()

        plt_aus_kat = aus_kat(df_aus_kat_sorted)
        plt_aus_kat.tight_layout()
        pdf_output.savefig(plt_aus_kat.gcf())
        plt_aus_kat.close()
        
        for plt_aus_kat_bes in aus_kat_bes(df_aus_bes_sorted):
            plt_aus_kat_bes.tight_layout()
            pdf_output.savefig(plt_aus_kat_bes.gcf())
            plt_aus_kat_bes.close()


