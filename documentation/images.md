## matplotlib_1.png
```python
fig, ax = plt.subplots(2, 2)
fig.set_size_inches(18.5, 10)
fig.suptitle('Diller arası karşılaştırma')

ax[0,0].scatter(azerice_max,azerice_min,color="red")
ax[0,0].scatter(uygurca_max,uygurca_min)
ax[0,0].set_title('Azerice - Uygurca')
ax[0,0].legend(['Azerice', 'Uygurca'])
ax[0,0].set(xlabel="MFCC MAX",ylabel="MFCC MİN")

ax[0,1].scatter(kazakca_max,kazakca_min,color="red")
ax[0,1].scatter(kirgizca_max,kirgizca_min)
ax[0,1].set_title('Kazakca - Kirgizca')
ax[0,1].legend(['Kazakca', 'Kirgizca'])
ax[0,1].set(xlabel="MFCC MAX",ylabel="MFCC MİN")

ax[1,0].scatter(azerice_max,azerice_min,color="red")
ax[1,0].scatter(uygurca_max,uygurca_min)
ax[1,0].set_title('Azerice - Uygurca')
ax[1,0].legend(['Azerice', 'Uygurca'])
ax[1,0].set(xlabel="MFCC MAX",ylabel="MFCC MİN")

ax[1,1].scatter(azerice_max,azerice_min,color="red")
ax[1,1].scatter(uygurca_max,uygurca_min)
ax[1,1].set_title('Azerice - Uygurca')
ax[1,1].legend(['Azerice', 'Uygurca'])
ax[1,1].set(xlabel="MFCC MAX",ylabel="MFCC MİN")

plt.savefig('example.png')
plt.show()
```