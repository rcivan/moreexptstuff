import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def main():
    expt_data = pd.read_csv('expt_data.csv')
    print(expt_data)

    plt.figure(figsize=(8,6))
    plt.plot(expt_data['exponent'], expt_data['min_runtime_old'], label='Old Method')
    plt.plot(expt_data['exponent'], expt_data['min_runtime_new'], label='New Method')
    #plt.plot(expt_data['exponent'], expt_data['min_runtime_builtin'], label='Builtin Method')
    plt.xlabel('Exponent')
    plt.ylabel('Runtime, seconds')
    plt.grid()
    plt.legend()
    plt.savefig('runtime.png')
    #plt.show()

    plt.figure(figsize=(8, 6))
    plt.plot(np.log(expt_data['exponent']), np.log(expt_data['min_runtime_old']), label='Old Method')
    plt.plot(np.log(expt_data['exponent']), np.log(expt_data['min_runtime_new']), label='New Method')
    #plt.plot(np.log(expt_data['exponent']), np.log(expt_data['min_runtime_builtin']), label='Builtin Method')
    plt.xlabel('log Exponent')
    plt.ylabel('log Runtime')
    plt.grid()
    plt.legend()
    plt.savefig('log_runtime.png')
    #plt.show()

if __name__ == '__main__':
    main()